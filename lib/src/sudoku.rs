use std::borrow::Borrow;
use std::fmt::{write, Debug, Display, Formatter};
use std::iter::{Enumerate, FilterMap};
use crate::error::CellError;

#[derive(Copy, Clone, Eq, PartialEq, Hash)]
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
impl Debug for Sudoku {
    
}
impl Default for Sudoku {
    fn default() -> Self {
        Self::new()
    }
}
impl Display for Sudoku {
    
}

/// A generic cell in a generic Sudoku grid.
/// It stores a value between 1 and N,
/// or a list of possible values if the exact value is unknown.
/// It is always valid since no methods allow for removal of every possible value.
#[derive(Copy, Clone, Eq, PartialEq, Hash)]
pub struct Cell<const N: usize = 9> {
    possible_values: [bool; N],
    possible_values_count: usize,
}
impl<const N: usize> Cell<N> {
    /// Create a new cell with an unknown value (all values possible).
    /// # Returns
    /// A new cell with all values possible.
    pub fn new() -> Self {
        Cell {
            possible_values: [true; N],
            possible_values_count: N,
        }
    }

    /// Create a new cell with a known value.
    /// # Arguments
    /// * `value` - The known value of the cell.
    /// # Returns
    /// * `Ok(cell)` If the value is valid.
    /// * `Err(error)` If the value is invalid.
    /// # Errors
    /// * [CellError::ValueOutOfRange] If the value is not between 1 and N.
    pub fn new_with_value(value: usize) -> Result<Self, CellError> {
        let mut cell = Cell::new();
        cell.set_value(value)?;
        Ok(cell)
    }

    /// Get the value of the cell.
    /// # Returns
    /// * `Some(value)` If the value is known.
    /// * `None` If the value is unknown (more than one possible value).
    pub fn get_value(&self) -> Option<usize> {
        if self.possible_values_count == 1 {
            for i in 0..N {
                if self.possible_values[i] {
                    return Some(i + 1);
                }
            }
        }
        None
    }

    /// Set the value of the cell to a known value.
    /// # Arguments
    /// * `value` - The value to set.
    /// # Returns
    /// * `Ok(changed)` If the value is valid.
    /// `true` if the cell's value changed, `false` if it didn't.
    /// * `Err(error)` If the value is invalid.
    /// # Errors
    /// * [CellError::ValueOutOfRange] If the value is not between 1 and N.
    pub fn set_value(&mut self, value: usize) -> Result<bool, CellError> {
        if value < 1 || value > N {
            Err(CellError::ValueOutOfRange)
        } else {
            let mut changed = self.possible_values[value - 1] == false;
            if changed {
                self.possible_values.fill(false);
                self.possible_values[value - 1] = true;
                self.possible_values_count = 1;
            } else {
                for i in 0..N {
                    if i != value - 1 && self.possible_values[i] {
                        self.possible_values[i] = false;
                        changed = true;
                        self.possible_values_count -= 1;
                        if self.possible_values_count == 1 {
                            break;
                        }
                    }
                }
            }
            Ok(changed)
        }
    }

    /// Get the ascending iterator of possible values for the cell.
    /// If the value is known, it will return an iterator with one value.
    /// If you need to get the number of possible values, use
    /// [Self::possible_values_count()] instead (more efficient).
    /// # Returns
    /// An ascending iterator of possible values for the cell.
    pub fn get_possible_values(&self) -> impl Iterator<Item=usize> {
        self.possible_values
            .iter()
            .enumerate()
            .filter_map(|(i, v)| if *v {Some(i + 1)} else {None})
    }

    /// Set the possible values for the cell.
    /// # Arguments
    /// * `possible_values` - The values to set.
    /// # Returns
    /// * `Ok(changed)` If the possible values are valid.
    /// `true` if the cell's possible values changed, `false` if they didn't.
    /// * `Err(error)` If the value is invalid.
    /// # Errors
    /// * [CellError::ValueOutOfRange] If any value is not between 1 and N.
    /// * [CellError::NoPossibleValues] If there are no values to set.
    pub fn set_possible_values<T, U>(&mut self, possible_values: T) -> Result<bool, CellError>
    where
        T: IntoIterator<Item=U>,
        U: Borrow<usize>,
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
    /// this always returns a value between 1 and N.
    /// # Returns
    /// The number of possible values for the cell.
    pub fn get_possible_values_count(&self) -> usize {
        self.possible_values_count
    }

    /// Check whether the value of the cell is known.
    /// # Returns
    /// * `true` if the value is known (only one possible value).
    /// * `false` if the value is unknown (more than one possible value).
    pub fn is_value_known(&self) -> bool {
        self.possible_values_count == 1
    }

    /// Check whether a value is possible for the cell.
    /// # Arguments
    /// * `value` - The value to check.
    /// # Returns
    /// * `Ok(true)` if the value is possible.
    /// * `Ok(false)` if the value is not possible.
    /// * `Err(error)` if the value is invalid.
    /// # Errors
    /// * [CellError::ValueOutOfRange] if the value is not between 1 and N.
    pub fn is_value_possible(&self, value: usize) -> Result<bool, CellError> {
        if value < 1 || value > N {
            return Err(CellError::ValueOutOfRange);
        }
        Ok(self.possible_values[value - 1])
    }

    /// Add a possible value to the cell.
    /// # Arguments
    /// * `value` - The value to add.
    /// # Returns
    /// * `Ok(false)` if the value was added successfully,
    /// but the value was already possible before adding
    /// * `Ok(true)` if the value was added successfully and the value was not possible before adding.
    /// * `Err(error)` if the value is invalid.
    /// # Errors
    /// * [CellError::ValueOutOfRange] if the value is not between 1 and N.
    pub fn add_possible_value(&mut self, value: usize) -> Result<bool, CellError> {
        if value < 1 || value > 9 {
            Err(CellError::ValueOutOfRange)
        } else {
            if self.possible_values[value - 1] {
                return Ok(false);
            }
            self.possible_values[value - 1] = true;
            Ok(true)
        }
    }

    /// Remove a possible value from the cell.
    /// # Arguments
    /// * `value` - The value to remove.
    /// # Returns
    /// * `Ok(true)` if the value was removed successfully and the value was possible before removing
    /// * `Ok(false)` if the value was already not possible before removing
    /// * `Err(error)` if the value is invalid.
    /// # Errors
    /// * [CellError::ValueOutOfRange] if the value is not between 1 and N.
    pub fn remove_possible_value(&mut self, value: usize) -> Result<bool, CellError> {
        if value < 1 || value > N {
            Err(CellError::ValueOutOfRange)
        } else if self.possible_values[value - 1] {
            self.possible_values[value - 1] = false;
            self.possible_values_count -= 1;
            if self.possible_values_count == 0 {
                return Err(CellError::NoPossibleValues);
            }
            Ok(true)
        } else {
            Ok(false)
        }
    }
}
impl Debug for Cell {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        write!(f, "Cell{{")?;
        match self.get_value() {
            Some(value) => write!(f, "{}", value)?,
            None => {
                let mut possible_values = self.get_possible_values();
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
impl Default for Cell {
    fn default() -> Self {
        Self::new()
    }
}
impl<const N: usize> Display for Cell<N> {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        let digits = N.ilog10() as usize + 1;
        match self.get_value() {
            Some(value) => write!(f, "{:>width$}", value, width=digits),
            None => write!(f, "{:>width$}", '.', width=digits),
        }
    }
}
impl<const N: usize> IntoIterator for Cell<N> {
    type Item = usize;
    type IntoIter = FilterMap<Enumerate<std::array::IntoIter<bool, N>>, fn((usize, bool)) -> Option<usize>>;

    fn into_iter(self) -> Self::IntoIter {
        self.possible_values
            .into_iter()
            .enumerate()
            .filter_map(|(i, v)| if v {Some(i + 1)} else {None})
    }
}
impl FromIterator<usize> for Result<Cell,CellError> {
    fn from_iter<T: IntoIterator<Item=usize>>(iter: T) -> Self {
        todo!()
    }
}
