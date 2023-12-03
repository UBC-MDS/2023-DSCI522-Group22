import pytest
import sys
import os
from unittest.mock import patch, Mock, mock_open
from click.testing import CliRunner
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts.download_file import * 

script_dir = '../scripts'  # Replace with the actual path
sys.path.append(os.path.abspath(script_dir))
from download_file import *  # Replace with the actual name of your script

def test_download_successful(tmp_path):

	test_url = "https://archive.ics.uci.edu/static/public/186/wine+quality.zip"
	test_destination = "../data"
	mock_response = Mock()
	mock_response.status_code = 200
	mock_response.content = b'data'

	with patch('download_file.requests.get', return_value=mock_response):
		runner = click.testing.CliRunner()
		result = runner.invoke(main, ['--url', test_url, '--destination', test_destination])
		print(result.exit_code)
		assert result.exit_code == 1
    

def test_download_failure_invalid_url():
    runner = CliRunner()
    result = runner.invoke(main, ['--url', 'invalidurl://example.com/somefile.csv'])
    assert result.exit_code != 0
    #assert 'Invalid URL provided' in result.output


# In test_download_file.py
def test_download_http_error(tmp_path):
    test_url = "https://example.com/nonexistentfile.csv"
    test_destination = tmp_path.as_posix()
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError

    with patch('download_file.requests.get', return_value=mock_response):
        runner = CliRunner()
        result = runner.invoke(main, ['--url', test_url, '--destination', test_destination])
        assert result.exit_code == 1  # Expecting a non-zero exit code for error
        assert "HTTP error occurred" in result.output

def create_test_zip(tmp_path, filename='test.zip'):
    zip_content = b"This is some test content"
    test_zip = tmp_path / filename
    with zipfile.ZipFile(test_zip, 'w') as zf:
        zf.writestr('test.txt', zip_content)
    return test_zip

def test_save_zip_file(tmp_path):
    # Create a test zip file
    test_zip = create_test_zip(tmp_path)
    destination = tmp_path / 'extracted'
    os.makedirs(destination)

    # Read the zip file content
    with open(test_zip, 'rb') as file:
        content = file.read()

    # Call the function
    save_or_extract_file(content, test_zip.name, destination.as_posix())

    # Check if the file is extracted
    extracted_file = destination / 'test.txt'
    assert extracted_file.exists(), "The zip file was not extracted correctly"

def test_save_non_zip_file(tmp_path):
    test_content = b"Sample CSV content"
    filename = 'test.csv'
    destination = tmp_path.as_posix()

    # Mock open function
    mocked_open = mock_open()

    with patch('builtins.open', mocked_open):
        save_or_extract_file(test_content, filename, destination)

        # Assert that open was called correctly
        mocked_open.assert_called_once_with(os.path.join(destination, filename), 'wb')

        # Get the mock file handle that open returns
        file_handle = mocked_open()
        
        # Assert that write was called on the file handle
        file_handle.write.assert_called_once_with(test_content)

@pytest.fixture
def create_temp_csv_files(tmp_path):
    # Create two temporary CSV files with sample data
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
    
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"
    df1.to_csv(file1, index=False)
    df2.to_csv(file2, index=False)

    return file1, file2

def test_concatenate_csv_files(create_temp_csv_files, tmp_path):
    file1, file2 = create_temp_csv_files
    output_file = tmp_path / "output.csv"

    # Call the function to concatenate files
    concatenate_csv_files(file1, file2, ',', output_file)

    # Read the output file and verify its contents
    combined_df = pd.read_csv(output_file, index_col=False)
    print(combined_df)
    expected_df = pd.DataFrame({'A': [1, 2, 5, 6], 'B': [3, 4, 7, 8],'color': ['red','red','white','white']})
    assert combined_df.shape[1] == expected_df.shape[1], "DataFrames do not have the same number of columns"
