//! Errors for the [ssudoku] library

use std::error::Error;
use std::fmt::Display;

#[derive(Debug, Copy, Clone, Eq, PartialEq, Hash)]
pub enum SudokuError {
    /// The value should be between 1 and 9 (inclusive).
    InvalidValue,
    /// The cell has no possible values.
    NoPossibleValues,
}
impl Display for SudokuError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        match self {
            SudokuError::InvalidValue => write!(f, "Invalid value (should be between 1 and 9)"),
            SudokuError::NoPossibleValues => write!(f, "No possible values for the cell"),
        }
    }
}
impl Error for SudokuError {}

#[derive(Debug, Copy, Clone, Eq, PartialEq, Hash)]
pub enum CellError {
    ValueOutOfRange,
    NoPossibleValues,
}
impl Display for CellError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        match self {
            CellError::Err1 => write!(f, "Error 1"),
        }
    }
}
impl Error for CellError {}
