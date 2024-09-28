use crate::error::Error;

#[derive(Debug, Copy, Clone, Eq, PartialEq, Hash)]
pub struct Cell {
    value: u8,
    possibilities: [bool; 9],
}
impl Cell {
    pub fn new() -> Self {
        Cell {
            value: 0,
            possibilities: [true; 9],
        }
    }
    
    fn get_value(&self) -> Option<u8> {
        self.value
    }
    
    fn set_value(&mut self, value: u8) -> Result<(), Error> {
        if value < 10 {
            self.value = value;
            Ok(())
        } else {
            Err(Error::InvalidValue)
        }
    }
}
impl Default for Cell {
    fn default() -> Self {
        Self::new()
    }
}

#[derive(Debug, Copy, Clone, Eq, PartialEq, Hash)]
pub struct Sudoku {
    cells: [[Cell; 9]; 9],
}
impl Sudoku {
    pub fn new() -> Self {
        Sudoku {
            cells: [[Cell::new(); 9]; 9],
        }
    }
    pub fn from_string(cells: &str) -> Result<Self, Error> {
        let cells = [[Cell::new(); 9]; 9];
        
    }
}
impl Default for Sudoku {
    fn default() -> Self {
        Self::new()
    }
}
