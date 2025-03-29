use std::error::Error as StdError;
use std::fmt::Display;

#[derive(Debug, Copy, Clone, Eq, PartialEq, Hash)]
pub enum Error {
    /// The value should be between 1 and 9 (inclusive).
    InvalidValue,
    /// The cell has no possible values.
    NoPossibleValues,
}
impl Display for Error {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        match self {
            Error::InvalidValue => write!(f, "Invalid value (should be between 1 and 9)"),
            Error::NoPossibleValues => write!(f, "No possible values for the cell"),
        }
    }
}
impl StdError for Error {}
