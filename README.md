
# 🦠 COVID-19 Data Visualization (India)

This project visualizes COVID-19 trends across Indian states using **Python**, **pandas**, and **matplotlib**. It includes bar charts, line plots, and pie charts to help understand the spread and impact of COVID-19 in India, particularly in Tamil Nadu and Maharashtra.

---

## 📊 Features

- **Bar Chart**: Confirmed cases by state (latest date).
- **Line Chart**: COVID-19 trend in Tamil Nadu (Confirmed, Recovered, Deaths).
- **Pie Chart**: Maharashtra case distribution (Recovered, Deaths, Active).

---

## 🛠 Requirements

Make sure the following Python libraries are installed:

```bash
pip install pandas matplotlib
````

---

## 📂 Project Files

* `main.py`: Main Python script for visualization.
* `covid_data.csv`: CSV file containing COVID-19 data.
* `README.md`: Project documentation.

---

## 📁 CSV Format

The `covid_data.csv` file should contain columns like:

```
Date,State,Confirmed,Recovered,Deaths
2021-01-01,Tamil Nadu,830000,810000,12200
2021-01-01,Maharashtra,1950000,1800000,50000
...
```

> 🔎 Make sure the column names match exactly or update them in the Python code accordingly.

---

## ▶️ How to Run

1. Place `main.py` and `covid_data.csv` in the same directory.
2. Run the script:

```bash
python main.py
```

3. The script will display:

   * A **bar chart** of confirmed cases by state.
   * A **line graph** showing Tamil Nadu’s COVID trend.
   * A **pie chart** showing the case distribution in Maharashtra.

---

## 🧠 Concepts Used

* Reading and cleaning CSV data using `pandas`
* Visualizing data using `matplotlib.pyplot`
* Creating:

  * Bar charts
  * Line plots with markers and legends
  * Pie charts with labels and color coding

---

## 📸 Sample Output

* Confirmed Cases by State (Bar Chart)
  ![image](https://github.com/user-attachments/assets/00ea160e-515f-420e-90fd-ea6deb2dee18)

* Tamil Nadu Trend (Line Plot)
  ![image](https://github.com/user-attachments/assets/ef85872e-e0c3-4c18-8751-f191b3896aec)

* Maharashtra Distribution (Pie Chart)
  ![image](https://github.com/user-attachments/assets/316f7930-b563-4466-bae1-3981127869f2)


---

## 📜 License

This project is for educational purposes only. No license restrictions.


