import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches 
#Data: Monthly orders fulfilled (in thousands) 
months = [f"M{i}" for i in range(1, 25)] 
orders = [52, 50, 53, 59, 51, 51, 60, 56, 51, 56, 52, 52, 56, 46, 47, 54, 52, 
51, 59, 54, 51, 66, 58, 60, 52] 
#Use first 24 values 
orders = orders[:24] 
#I-Chart calculations  
mean_x = np.mean(orders) 
#Moving Range (MR) 
mr = [abs(orders[i] - orders[i-1]) for i in range(1, len(orders))] 
mean_mr = np.mean(mr) 
#Control limits using d2 = 1.128 for n=2 
d2 = 1.128 
sigma = mean_mr / d2 
UCL_x = mean_x + 3 * sigma 
LCL_x = mean_x - 3 * sigma 
#MR-Chart calculations 
D4 = 3.267  # for n=2 
D3 = 0      
# for n=2 
UCL_mr = D4 * mean_mr 
LCL_mr = D3 * mean_mr  # = 0 
#Plotting 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 9), sharex=False) 
fig.patch.set_facecolor('white') 
x = np.arange(len(months)) 
x_mr = np.arange(1, len(months))  # MR starts from M2 
#I-Chart (top) 
ax1.set_facecolor('white') 
ax1.grid(True, color='lightgray', linewidth=0.7, zorder=0) 
ax1.plot(x, orders, color='blue', marker='o', markersize=5, 
linewidth=1.5, label='Individual Value', zorder=3) 
P a ge 51 | 70 
C I S- 202510-CDS2433-G roup Project  
ax1.axhline(mean_x, color='green', linestyle='--', linewidth=1.5, 
label='Mean', zorder=2) 
ax1.axhline(UCL_x,  color='red',   linestyle='--', linewidth=1.5, label='UCL', 
zorder=2) 
ax1.axhline(LCL_x,  color='red',   linestyle='--', linewidth=1.5, label='LCL', 
zorder=2) 
ax1.set_title('I-Chart: Number of Orders Fulfilled (in thousands)', 
fontsize=13, fontweight='bold', pad=10) 
ax1.set_ylabel('Orders (k)', fontsize=11) 
ax1.set_xticks(x) 
ax1.set_xticklabels(months, fontsize=8) 
ax1.legend(loc='upper right', fontsize=9, framealpha=1) 
ax1.set_ylim(38, 72) 
#Annotate control limit values on right side 
ax1.annotate(f'{UCL_x:.1f}', xy=(23.6, UCL_x), fontsize=8, color='red', 
va='center') 
ax1.annotate(f'{mean_x:.1f}', xy=(23.6, mean_x), fontsize=8, color='green', 
va='center') 
ax1.annotate(f'{LCL_x:.1f}', xy=(23.6, LCL_x), fontsize=8, color='red', 
va='center') 
#MR-Chart (bottom) 
ax2.set_facecolor('white') 
ax2.grid(True, color='lightgray', linewidth=0.7, zorder=0) 
ax2.plot(x_mr - 1, mr, color='magenta', marker='s', markersize=5, 
linewidth=1.5, label='Moving Range', zorder=3) 
ax2.axhline(mean_mr, color='green', linestyle='--', linewidth=1.5, label='Mean 
MR', zorder=2) 
ax2.axhline(UCL_mr,  color='red',   linestyle='--', linewidth=1.5, 
label='UCL', zorder=2) 
ax2.axhline(LCL_mr,  color='red',   linestyle='--', linewidth=1.5, 
label='LCL', zorder=2) 
ax2.set_title('MR-Chart: Moving Range of Orders', 
fontsize=13, fontweight='bold', pad=10) 
ax2.set_ylabel('Moving Range', fontsize=11) 
ax2.set_xlabel('Month', fontsize=11) 
ax2.set_xticks(x_mr - 1) 
ax2.set_xticklabels(months[1:], fontsize=8) 
ax2.legend(loc='upper right', fontsize=9, framealpha=1) 
ax2.set_ylim(-0.5, 18) 
#Annotate control limit values on right side 
P a ge 52 | 70 
C I S- 202510-CDS2433-G roup Project  
ax2.annotate(f'{UCL_mr:.1f}', xy=(22.6, UCL_mr), fontsize=8, color='red', 
va='center') 
ax2.annotate(f'{mean_mr:.1f}', xy=(22.6, mean_mr), fontsize=8, color='green', 
va='center') 
ax2.annotate(f'{LCL_mr:.1f}', xy=(22.6, LCL_mr), fontsize=8, color='red', 
va='center') 
plt.tight_layout(pad=2.5) 
plt.savefig('/home/ubuntu/control_chart_noon.png', dpi=150, 
bbox_inches='tight', 
facecolor='white') 
plt.show() 
print("Chart saved to /home/ubuntu/control_chart_noon.png") 
#Print summary 
print(f"\n=== I-Chart Summary ===") 
print(f"Mean (X̄ )  = {mean_x:.2f}k orders") 
print(f"UCL       
= {UCL_x:.2f}k orders") 
print(f"LCL       
= {LCL_x:.2f}k orders") 
print(f"\n=== MR-Chart Summary ===") 
print(f"Mean MR   = {mean_mr:.2f}k orders") 
print(f"UCL_MR    
= {UCL_mr:.2f}k orders") 
print(f"LCL_MR    
= {LCL_mr:.2f}k orders (= 0)")