# 📊 Business Process Modelling & Optimization - Noon.com Order Fulfillment

This repository contains the project documentation for the **Business Process Modelling & Optimization** project (CDS 2433). The project focuses on analyzing and optimizing the **Customer Order Fulfillment (Directship Model)** process at Noon.com.

---

## 🚀 Project Overview

Noon.com, a leading e-commerce platform, faces challenges in its order fulfillment process, particularly within its direct-ship model. The manual and often inefficient nature of current operations leads to delays, increased costs, and potential customer dissatisfaction. This project aims to identify bottlenecks, non-value-added activities, and areas for improvement within Noon's existing (AS-IS) order fulfillment process.

Through detailed analysis and simulation, we propose an optimized (TO-BE) process model designed to enhance efficiency, reduce cycle time, and minimize operational costs.

### Key Objectives:
- **Analyze** the current AS-IS order fulfillment process at Noon.com.
- **Model** the process using Business Process Model and Notation (BPMN).
- **Quantitatively analyze** the process for time, cost, and variability.
- **Propose and simulate** an optimized TO-BE process model.
- **Recommend** practical enhancements for improved operational efficiency.

---

## 🛠️ Methodology & Tools

Our approach involved a comprehensive methodology combining process modeling, qualitative and quantitative analysis, and advanced simulation techniques:

- **Business Process Model and Notation (BPMN):** Used to visually represent both the AS-IS and TO-BE processes, providing a clear, standardized understanding of the workflow.
- **Qualitative Analysis:** Included Value-Added Analysis (VA, BVA, NVA) and Waste Analysis (Lean principles).
- **Quantitative Analysis:** Focused on time (Cycle Time Efficiency), cost (Labor Cost Analysis), and process variability (I-MR Control Charts).
  
- **Service-Oriented Architecture (SOA):** Designed RESTful web services for cross-pool communication, mapping BPMN tasks to API specifications (GET, POST, PUT).
- **Decision Model and Notation (DMN):** Utilized to model complex decision-making logic, specifically for payment authorization.
- **Bizagi Modeler & Simulator:** Employed for process execution and simulation across four levels:
    1.  **Process Validation:** Ensuring logical correctness and routing.
    2.  **Time Analysis:** Measuring end-to-end cycle time under infinite resource capacity.
    3.  **Resource Analysis:** Identifying bottlenecks and optimizing resource utilization.
    4.  **Calendars Analysis:** Modeling real-world operational scenarios with working hours.

---

## 🔍 AS-IS Process Analysis (Customer Order Fulfillment)

Our analysis of Noon.com's existing order fulfillment process revealed several areas for improvement:

<img width="2631" height="2072" alt="Noons New Model" src="https://github.com/user-attachments/assets/4d5f03f9-04d7-4f7c-8dd4-b43b47550f96" />

### Value-Added Analysis:
We classified 20 tasks within the process, identifying several **Non-Value-Added (NVA)** activities:
*   `Submit pickup request`: A manual coordination step causing waiting time.
*   `Deliver to Noon's warehouse`: Pure transportation and waiting step.
*   `Schedule Re-delivery attempt`: Rework caused by failed initial delivery.
*   `Return shipment to origin`: Waste/rework due to ultimate delivery failure.

### Waste Analysis (Lean Principles):
Identified key wastes:
*   **Transportation:** Double handling of packages (Seller → Noon warehouse → Customer).
*   **Waiting:** Delays for logistics carrier pickup and warehouse sorting.
*   **Overprocessing:** Multiple scans of shipment details.
*   **Defects/Rework:** Failed deliveries leading to re-delivery attempts or returns.

### Quantitative Analysis:
*   **Time Analysis:**
    *   **Total Cycle Time (AS-IS):** 324 minutes.
    *   **Cycle Time Efficiency (CTE):** 29.6% (indicating heavy burden from waiting times).
    *   **Primary Bottlenecks:** `Deliver to customer` (145 mins), `Deliver to Noon’s warehouse` (90 mins), `Pick product from inventory` (45 mins).
*   **Cost Analysis:**
    *   **Total Labor Cost per Order:** 32.58 AED.
    *   **Highest Cost Contributor:** Logistics Driver (24.58 AED/order), requiring the highest FTE (62 drivers for 500 orders/day).
*   **Process Variability (I-MR Control Chart):** Analysis of 24 months of simulated order data showed the process was statistically stable and in control, with no special causes of variation, even during seasonal spikes (e.g., 
Yellow Friday sales), allowing for reliable capacity forecasting.

<img width="502" height="310" alt="image" src="https://github.com/user-attachments/assets/86426f2a-2b74-4159-a1eb-1cda57dc4d73" />


---

## ✨ TO-BE Process Optimization & Simulation

Based on our analysis, we designed an optimized TO-BE process model, focusing on automation, efficiency, and improved customer experience. This model was rigorously simulated using Bizagi Modeler.

### Decision-Making Logic (DMN):
We implemented a DMN table for **Payment Authorization**, ensuring secure and efficient order processing. This logic prioritizes risk management by flagging high-value transactions (>10,000 AED or COD > 500 AED) for manual review, while automating approvals for legitimate transactions and declines for fraudulent ones.

### Bizagi Simulation Results (TO-BE Model):

**Level 1: Process Validation**
*   Confirmed the BPMN model's syntactic correctness and behavioral soundness. All 100 simulated order instances completed successfully with no routing errors, validating the logic of gateways (e.g., 95% payment approved, 88% delivery successful).

**Level 2: Time Analysis**
*   **Average Cycle Time (TO-BE):** Significantly improved to approximately **181 minutes** (3h 1m 8s) from the AS-IS 324 minutes. This reduction is attributed to automated routing and DMN-based decisions eliminating non-value-added waiting time.
*   **Longest Task (Avg):** `Deliver to Customer` (54m 20s).

**Level 3: Resource Analysis**
*   **Bottleneck Identified:** Warehouse Staff showed high utilization (81%), indicating a potential bottleneck if order volume increases. Bizagi suggested considering an additional staff member.
*   **Resource Utilization:** Logistics Driver (72%), OMS System (58%).
*   **Impact:** For the current arrival rate, existing resources are just sufficient, but there is no room for growth without optimization.

**Level 4: Calendars Analysis**
*   Introduced real-world working calendars for resources (e.g., Seller Staff: Mon-Fri, 9 AM-6 PM). This revealed the creation of **overnight queues** for orders placed after seller closing times, significantly increasing cycle time for evening/night orders.
*   **Strategic Insight:** This justifies differentiating sellers based on Service Level Agreements (SLAs) and dynamically adjusting promised delivery times based on seller type and time of day, aligning with our DMN model.

---

## 💡 Recommendations for Further Enhancement

To further optimize Noon.com's order fulfillment process, we recommend:
1.  **Predictive Analytics for Logistics:** Integrate Machine Learning models to forecast order volumes by geographic zone, enabling prepositioning of delivery vans and reducing 
Travel to Seller Warehouse" time.
2.  **Encourage Seller Competition:** Utilize the BPMS dashboard to display real-time seller performance (e.g., packing speed), fostering friendly competition to improve efficiency.
3.  **Automated Exception Handling:** Enhance the BPMS to automatically trigger SMS notifications to customers for rescheduling failed deliveries, reducing manual intervention.

---

## 💡 My Role & Key Learnings

As a member of this project, my contributions were focused on the Service-Oriented Architecture (SOA) design and its integration with the BPMN process.

*   **SOA Design:** I focused on defining web services for critical cross-pool communication tasks such as `Complete Checkout`, `Authorize Payment Transaction`, `Receive Order`, `Submit Pickup Request`, `Receive Pickup Task`, `Update Status to Shipped`, and `Capture Proof of Delivery`.
*   **RESTful API Specification:** I meticulously analyzed the data flow to link each BPMN task to a web service, ensuring the correct HTTP VERB (GET, POST, PUT) was used based on RESTful principles. For instance, `POST` for creating new transactions and `PUT` for modifying existing order statuses.
*   **JSON Data Structuring:** I gained valuable insights into structuring JSON data for API requests and responses, understanding the nuances of using arrays versus objects.
*   **URI Design:** I learned the importance of designing detailed URI paths that reflect resource hierarchy for better architectural alignment with the BPMN process.

This project significantly deepened my understanding of how business processes are translated into technical architectures, emphasizing the importance of clear communication between process models and API specifications.

---

## 👥 Team & Acknowledgements

This project was a collaborative effort by a dedicated team:
*   **Maryam Ali Alali:** (H00535836) - Focused on SOA design, API specifications, and JSON structuring.
*   **Hessa Khalfan Al Ali:** (H00535166) - Focused on NVA elimination recommendations, quantitative analysis (data simulation, Python code for Control Chart), and DMN table construction.
*   **Nourah Abdulla Alghfeli:** (H00535834) - Focused on Waste Analysis, Quantitative Analysis (Cost), and detailed interpretation of the Control Chart.

---

## 📄 Project Documentation & Assets

*   **Full Project Report (PDF) contains:**
*   **1- BPMN Models:** AS-IS and TO-BE process diagrams.
*   **2- DMN Table:** Payment Authorization Decision Logic.
*   **3- Bizagi Simulation Results:** Detailed reports from Level 1, 2, 3, and 4 simulations.
*   **4- Python Code:** For I-MR Control Chart generation.

*(Note: All figures mentioned in the report, including BPMN diagrams, control charts, and Bizagi simulation screenshots, are available in the full project report PDF.)*
