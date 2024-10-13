## Project name: Determination of Radical Scavenging Activity in Vegetable Oils Using Smartphone Image Analysis in the RGB Colour System

This project provides a Python-based tool to determine the radical scavenging activity (RSA) using RGB values extracted from smartphone images of samples. The RGB colour system is used to compute values that are then used to estimate the RSA of various samples.

### Features

- **RSA Calculation**: Calculates radical scavenging activity (RSA) using RGB channels from images.
- **Interactive Input**: Users provide `I0`, `IDPPH`, and the RGB values for each sample, and the tool calculates the corresponding RSA.
- **Data Export**: Results are saved in an Excel file for easy sharing and analysis.

### Workflow

1. **Input**: Users enter the `I0` and `IDPPH` values, as well as the RGB values for each sample.
2. **RSA Calculation**: The program calculates `ADPPH`, `Aoil`, and the final RSA values for each sample.
3. **Output**: Results are saved in an Excel file, containing the sample names, RGB values, and the calculated RSA values.

### Example Usage

1. Input the required `I0`, `IDPPH`, and sample data.
2. Input the RGB values for each sample when prompted.
3. Save the results in an Excel file for further analysis.

### Dependencies

- Python 3.x
- Math
- Pandas

Install the required libraries via pip:

```bash
pip install pandas
```
Once the dependencies are installed, you can proceed to run the script and input your data for analysis.

### License

This project is licensed under the **GNU General Public License v3.0**. You are free to use, modify, and distribute the code for academic and non-commercial purposes. However, any commercial usage may require a separate license.
