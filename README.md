# 📊 Business Process Modelling & Optimization - Noon.com Order Fulfillment

This repository contains the project documentation for the **Business Process Modelling & Optimization** project (CDS 2433). The project focuses on analyzing and optimizing the **Customer Order Fulfillment (Directship Model)** process at Noon.com.

<p align="center">
  <img src="https://img.shields.io/badge/Python-Data%20Analysis-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Bizagi-Process%20Simulation-orange?style=for-the-badge" alt="Bizagi">
  <img src="https://img.shields.io/badge/BPMN%20%26%20DMN-Modeling-green?style=for-the-badge" alt="BPMN">
</p>

---

## 🚀 Project Overview

Noon.com, a leading e-commerce platform, faces challenges in its order fulfillment process, particularly within its direct-ship model. The manual and often inefficient nature of current operations leads to delays, increased costs, and potential customer dissatisfaction. 

This project aims to identify bottlenecks, non-value-added activities, and areas for improvement within Noon's existing (AS-IS ) order fulfillment process. Through detailed analysis and simulation, we propose an optimized (TO-BE) process model designed to enhance efficiency, reduce cycle time, and minimize operational costs.

---

## 💡 My Role & Contributions (Hessa Khalfan)

As a core analyst on this project, my contributions focused heavily on **quantitative analysis, statistical programming, and decision logic modeling**:

*   **Statistical Process Control (Python):** I wrote the Python scripts to generate and analyze **I-MR Control Charts**. This involved simulating 24 months of order data to evaluate process variability, ensuring the system remained statistically stable even during seasonal spikes (e.g., Yellow Friday sales).
*   **Decision Modeling (DMN):** I constructed the Decision Model and Notation (DMN) tables for the Payment Authorization logic. This automated the risk management process, flagging high-value transactions for manual review while instantly approving legitimate ones.
*   **Quantitative & Waste Analysis:** I conducted deep quantitative analysis to identify bottlenecks and formulated strategic recommendations for Non-Value-Added (NVA) activity elimination, directly contributing to the reduction of the overall cycle time.

This project significantly deepened my ability to merge business process management with data-driven statistical analysis using Python.

---

## 🛠️ Methodology & Tools

*   **BPMN & DMN:** Used to visually represent workflows and complex decision-making logic.
*   **Bizagi Modeler & Simulator:** Employed for process execution and simulation across four levels (Process Validation, Time Analysis, Resource Analysis, Calendars Analysis).
*   **Python:** Utilized for data simulation and generating I-MR Control Charts.
*   **Qualitative Analysis:** Value-Added Analysis (VA, BVA, NVA) and Lean Waste Analysis.

---

## 🔍 AS-IS Process Analysis & Optimization

Our analysis of Noon.com's existing order fulfillment process revealed several areas for improvement:

<p align="center">
  <img width="100%" alt="Noons New Model" src="https://github.com/user-attachments/assets/4d5f03f9-04d7-4f7c-8dd4-b43b47550f96" />
</p>

### Quantitative Analysis & Process Variability:
Analysis of 24 months of simulated order data showed the process was statistically stable and in control, with no special causes of variation, allowing for reliable capacity forecasting.

<p align="center">
  <img width="70%" alt="Control Chart" src="https://github.com/user-attachments/assets/86426f2a-2b74-4159-a1eb-1cda57dc4d73" />
</p>

### Key Findings & Optimization (TO-BE Model )
*   **Cycle Time Reduction:** The optimized TO-BE model reduced the average cycle time from **324 minutes** to approximately **181 minutes**, largely by eliminating NVA waiting times through automated routing.
*   **Resource Optimization:** Identified Warehouse Staff as a primary bottleneck (81% utilization) and modeled capacity adjustments to handle future growth.
*   **SLA Strategy:** Calendar analysis revealed overnight queuing issues, leading to a strategic recommendation to implement dynamic delivery SLAs based on seller operational hours.

---

## 📁 Project Documentation & Assets

*   **[📄 Read the Full Project Report (PDF)](Full_Project_Report.pdf)** *(Includes BPMN Models, DMN Tables, and Bizagi Simulation Results)*
*   **[🐍 View the Python Code for Control Charts](Control_Chart_Analysis.py)**

*(Note: The full BPMN files and Python scripts are available in this repository).*
