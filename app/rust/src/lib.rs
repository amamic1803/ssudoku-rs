use sudoku::Sudoku;
use pyo3::prelude::*;

#[pyfunction]
fn solve_sudoku(sudoku_line: &str) -> PyResult<String> {
    let sudoku = Sudoku::from_str_line(sudoku_line).unwrap();
    return if let Some(solution) = sudoku.solve_unique() {
        Ok(solution.to_str_line().to_string())
    } else {
        Ok("0".to_string())
    }
}

#[pymodule]
fn rust(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(solve_sudoku, m)?)?;
    Ok(())
}
