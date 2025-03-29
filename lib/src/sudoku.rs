use std::borrow::Borrow;
use std::fmt::{write, Display, Formatter};
use std::iter;
use crate::error::Error;



#[derive(Debug, Copy, Clone, Eq, PartialEq, Hash)]
pub struct Sudoku {
    cells: [[Cell; 9]; 9],
}
impl Sudoku {
    const BLOCK_SIZE: usize = 3;
    const SIZE: usize = Self::BLOCK_SIZE * Self::BLOCK_SIZE;
    
    pub fn new() -> Self {
        Sudoku {
            cells: [[Cell::new(); Self::SIZE]; Self::SIZE],
        }
    }
    pub fn from_string(cells: &str) -> Result<Self, Error> {
        let mut cells_grid = [[Cell::new(); Self::SIZE]; Self::SIZE];
        
        let mut i = 0;
        for c in cells.chars() {
            match c {
                '1'..='9' => {
                    cells_grid[i / Self::SIZE][i % Self::SIZE].set_value(c.to_digit((Self::SIZE + 1) as u32).unwrap() as u8)?;
                    i += 1;
                }
                '.' => {
                    i += 1;
                }
                _ => {}
            }
        }
        if i < Self::SIZE * Self::SIZE {
            return Err(Error::NotEnoughCells);
        }
        
        Ok(Self { cells: cells_grid })
    }
}
impl Default for Sudoku {
    fn default() -> Self {
        Self::new()
    }
}

/// A cell in a Sudoku grid.
/// It stores a value between 1 and 9, or possible values if the exact value is not known.
/// [Cell] is always valid since no methods allow for removal of all possible values
/// (1 must always be possible, known).
#[derive(Debug, Copy, Clone, Eq, PartialEq, Hash)]
pub struct Cell {
    possible_values: u16,
}
impl Cell {
    /// Create a new cell with an unknown value (all values 1 to 9 are possible).
    /// # Returns
    /// A new cell with all values possible.
    pub fn new() -> Self {
        Cell {
            possible_values: 0b0000001111111110,
        }
    }

    /// Create a new cell with a known value.
    /// # Arguments
    /// * `value` - The known value.
    /// # Returns
    /// * `Ok(cell)` if the value is valid.
    /// * `Err(error)` if the value is invalid.
    /// # Errors
    /// * [Error::InvalidValue] if the value is not between 1 and 9.
    pub fn new_with_value(value: u8) -> Result<Self, Error> {
        let mut cell = Cell::new();
        cell.set_value(value)?;
        Ok(cell)
    }

    /// Get the value of the cell.
    /// # Returns
    /// * `Some(value)` if the value is known (equivalent to only one value being possible).
    /// * `None` if the value is unknown.
    pub fn value(&self) -> Option<u8> {
        match self.possible_values {
            0b0000000000000010 => Some(1),
            0b0000000000000100 => Some(2),
            0b0000000000001000 => Some(3),
            0b0000000000010000 => Some(4),
            0b0000000000100000 => Some(5),
            0b0000000001000000 => Some(6),
            0b0000000010000000 => Some(7),
            0b0000000100000000 => Some(8),
            0b0000001000000000 => Some(9),
            _ => None,
        }
    }

    /// Set the cell to a known value.
    /// # Arguments
    /// * `value` - The value to set.
    /// # Returns
    /// * `Ok(changed)` if the value is valid and set successfully
    /// (`true` if the cell's value changed, `false` if it didn't).
    /// * `Err(error)` if the value is invalid.
    /// # Errors
    /// * [Error::InvalidValue] if the value is not between 1 and 9.
    pub fn set_value(&mut self, value: u8) -> Result<bool, Error> {
        if value < 1 || value > 9 {
            Err(Error::InvalidValue)
        } else {
            let prev_poss_val = self.possible_values;
            self.possible_values = 1 << value;
            Ok(prev_poss_val != self.possible_values)
        }
    }

    /// Get the iterator of possible values for the cell.
    /// It always starts with the smallest possible value.
    /// Note that this function always returns a valid iterator because,
    /// even in cases when the value is known,
    /// it will return an iterator with one value.
    /// If you need to get the number of possible values, use [Self::possible_values_count()] instead of
    /// counting the number of elements in this iterator (more efficient).
    /// # Returns
    /// An iterator over the possible values for the cell.
    pub fn possible_values(&self) -> impl Iterator<Item=u8> {
        let mut possible_values = self.possible_values;
        iter::from_fn(move || {
            if possible_values == 0 {
                None
            } else {
                let trail_zeros = possible_values.trailing_zeros() as u8;
                possible_values &= !(1 << trail_zeros);
                Some(trail_zeros)
            }
        })
    }

    /// Set the possible values for the cell.
    /// # Arguments
    /// * `possible_values` - The possible values to set.
    /// # Returns
    /// * `Ok(changed)` if the possible values are set successfully
    /// (`true` if the cell's value changed, `false` if it didn't).
    /// * `Err(error)` if the value is invalid.
    /// # Errors
    /// * [Error::InvalidValue] if any value is not between 1 and 9.
    /// * [Error::NoPossibleValues] if there are no possible values to set.
    pub fn set_possible_values<T, U>(&mut self, possible_values: T) -> Result<bool, Error> 
    where
        T: IntoIterator<Item=U>,
        U: Borrow<u8>,
    {
        let mut new_possible_values = 0;
        for value in possible_values.into_iter().map(|value| *value.borrow()) {
            if value < 1 || value > 9 {
                return Err(Error::InvalidValue);
            }
            new_possible_values |= 1 << value;
        }
        if new_possible_values == 0 {
            return Err(Error::NoPossibleValues);
        }
        let changed = self.possible_values != new_possible_values;
        self.possible_values = new_possible_values;
        Ok(changed)
    }

    /// Get the number of possible values for the cell.
    /// If the value is known, it will return 1.
    /// Since the cell can't be empty (must have at least one possible value),
    /// this always returns a value between 1 and 9.
    /// # Returns
    /// The number of possible values for the cell.
    pub fn possible_values_count(&self) -> u8 {
        self.possible_values.count_ones() as u8
    }

    /// Check whether a value is possible for the cell.
    /// # Arguments
    /// * `value` - The value to check.
    /// # Returns
    /// `true` if the value is possible, `false` otherwise.
    pub fn is_value_possible(&self, value: u8) -> bool {
        self.possible_values & (1 << value) != 0
    }

    /// Add a possible value to the cell.
    /// # Arguments
    /// * `value` - The value to add.
    /// # Returns
    /// * `Ok(())` if the value was added successfully.
    /// * `Err(error)` if the value is invalid.
    /// # Errors
    /// * [Error::InvalidValue] if the value is not between 1 and 9.
    pub fn add_possible_value(&mut self, value: u8) -> Result<(), Error> {
        if value < 1 || value > 9 {
            Err(Error::InvalidValue)
        } else {
            self.possible_values |= 1 << value;
            Ok(())
        }
    }

    /// Remove a possible value from the cell.
    /// # Arguments
    /// * `value` - The value to remove.
    /// # Returns
    /// * `Ok(known)` if the value is removed successfully
    /// (`true` if the value of the cell is now known, `false` otherwise).
    /// * `Err(error)` if the value is invalid.
    /// # Errors
    /// * [Error::InvalidValue] if the value is not between 1 and 9.
    pub fn remove_possible_value(&mut self, value: u8) -> Result<bool, Error> {
        if value < 1 || value > 9 {
            Err(Error::InvalidValue)
        } else {
            self.possible_values &= !(1 << value);
            Ok(self.possible_values_count() == 1)
        }
    }
}
impl Default for Cell {
    fn default() -> Self {
        Self::new()
    }
}
impl Display for Cell {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "Cell{{")?;
        match self.value() {
            Some(value) => write!(f, "{}", value)?,
            None => {
                let mut possible_values = self.possible_values();
                if let Some(value) = possible_values.next() {
                    write!(f, "{}", value)?;
                }
                for value in possible_values {
                    write!(f, ",{}", value)?;
                }
            }
        }
        write!(f, "}}")
    }
}
