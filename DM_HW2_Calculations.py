

# Homework_2

# Question 1
"""


print("Question 6")
"""# Question 6"""

def calculate_gini(probabilities):
    gini_value = 0
    for probability in probabilities:
        gini_value += probability ** 2
    return 1 - gini_value

# (a)

# For root node

gini_above_root_x5 = calculate_gini([1, 0])
gini_below_root_x5 = calculate_gini([0.26/0.5, 0.24/0.5])
weighted_gini_index_root = 0.5 * gini_below_root_x5 + 0.5 * gini_above_root_x5

gini_above_root_y4 = calculate_gini([0.36/0.6, 0.24/0.6])
gini_below_root_y4 = calculate_gini([1])
weighted_gini_index_root_y4 = 0.4 * gini_below_root_y4 + 0.6 * gini_above_root_y4

gini_above_root_y7 = calculate_gini([0.21/0.3, 0.09/0.3])
gini_below_root_y7 = calculate_gini([0.55/0.7, 0.15/0.7])
weighted_gini_index_root_y7 = 0.7 * gini_below_root_y7 + 0.3 * gini_above_root_y7

gini_above_root_x2 = calculate_gini([0.62/0.8, 0.18/0.8])
gini_below_root_x2 = calculate_gini([0.14/0.2, 0.06/0.2])
weighted_gini_index_root_x2 = 0.2 * gini_below_root_x2 + 0.8 * gini_above_root_x2

print("Gini index for above x<0.5:", gini_above_root_x5)
print("Gini index for below x<0.5:", gini_below_root_x5)
print("Weighted Gini index for x<0.5:", weighted_gini_index_root)
print()
print("Gini index for above y<0.4:", gini_above_root_y4)
print("Gini index for below y<0.4:", gini_below_root_y4)
print("Weighted Gini index for y<0.4:", weighted_gini_index_root_y4)
print()
print("Gini index for above y<0.4:", gini_above_root_y7)
print("Gini index for below y<0.4:", gini_below_root_y7)
print("Weighted Gini index for y<0.4:", weighted_gini_index_root_y7)
print()
print("Gini index for above x<0.2:", gini_above_root_x2)
print("Gini index for below x<0.2:", gini_below_root_x2)
print("Weighted Gini index for x<0.2:", weighted_gini_index_root_x2)

"""## Root node will be x<=0.5"""

# Level 2 left

gini_above_y4_lx5 = calculate_gini([0.06/0.3, 0.24/0.3])
gini_below_y4_lx5 = calculate_gini([1, 0])
weighted_gini_y4_lx5 = (0.3/0.5) * gini_above_y4_lx5

gini_above_y7_lx5 = calculate_gini([0.06/0.15, 0.09/0.15])
gini_below_y7_lx5 = calculate_gini([0.2/0.35, 0.15/0.35])
weighted_gini_y7_lx5 = (0.15/0.5) * gini_above_y7_lx5 + (0.35/0.5) * gini_below_y7_lx5

gini_above_x2_lx5 = calculate_gini([0.14/0.2, 0.06/0.2])
gini_below_x2_lx5 = calculate_gini([0.12/0.3, 0.18/0.3])
weighted_gini_x2_lx5 = (0.3/0.5) * gini_above_x2_lx5 + (0.2/0.5) * gini_below_x2_lx5

print("Weighted Gini index for y<0.4 and x<0.5:", weighted_gini_y4_lx5)
print("Gini index for less y<0.4 and x<0.5:", gini_below_y4_lx5)
print("Gini index for above y<0.4 and x<0.5:", gini_above_y4_lx5)
print()
print("Weighted Gini index for y<0.7 and x<0.5:", weighted_gini_y7_lx5)
print("Gini index for above y<0.7 and x<0.5:", gini_above_y7_lx5)
print("Gini index for less y<0.7 and x<0.5:", gini_below_y7_lx5)
print()
print("Gini index for x > 0.5:", gini_above_x2_lx5)
print("Gini index for x <= 0.5:", gini_below_x2_lx5)
print("Weighted Gini index for y > 0.7, x <= 0.5:", weighted_gini_x2_lx5)

"""# Left node will be y<=0.4"""

# Level 2 right

gini_above_y7_gx5 = calculate_gini([0.15/0.15, 0/0.15])
gini_below_y7_gx5 = calculate_gini([0.35/0.35, 0/0.35])
weighted_gini_y7_gx5 = (0.15/0.5) * gini_above_y7_gx5 + (0.35/0.5) * gini_below_y7_gx5

gini_above_x2_gx5 = calculate_gini([0.5/0.5, 0])
gini_below_x2_gx5 = calculate_gini([0, 0])
weighted_gini_x2_gx5 = 0 * gini_below_x2_gx5 + gini_above_x2_gx5 * (0.5/0.5)

print("Gini index for y > 0.7:", gini_above_y7_gx5)
print("Gini index for y <= 0.7:", gini_below_y7_gx5)
print("Weighted Gini index for y > 0.7, x > 0.5:", weighted_gini_y7_gx5)
print()

# Print results
print("Gini index for x > 0.5:", gini_above_x2_gx5)
print("Gini index for x <= 0.5:", gini_below_x2_gx5)
print("Weighted Gini index for x > 0.5, x > 0.5:", weighted_gini_x2_gx5)

# (b)

print("Misclassification X coordinates = 0.0 to 0.2")
print("Misclassification Y coordinates = 0.7 to 1.0")
print("So any data point chosen out of this area of 0.2*0.3 = 0.06 will be misclassified ")

error_rate = 0.2 * 0.3
print(error_rate)



print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")


print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")
print("Question 2")


#(a)

import math

parent_entropy_value = -(0.41*math.log(0.41,2)+0.46*math.log(0.46,2)+0.13*math.log(0.13,2))
parent_entropy_value

#(b)

# For x <= 0.2

x_2_left_value = -(0.04/0.2)*(math.log((0.04/0.2),2))-(0.16/0.2)*(math.log((0.16/0.2),2))

x_2_right_value = -((0.41/0.8)*math.log((0.41/0.8),2) + (0.3/0.8) * math.log((0.3/0.8),2) + (0.09/0.8) * math.log((0.09/0.8),2))

x_2_weighted_value = 0.2*x_2_left_value + 0.8 *x_2_right_value

info_gain_x_2_value = parent_entropy_value - x_2_weighted_value

# For x <= 0.7

x_7_left_value = -((0.2 / 0.7)*(math.log((0.2 / 0.7),2))+(0.459999 / 0.7)*(math.log((0.459999 / 0.7),2))+(0.04/0.7)*(math.log((0.04/0.7),2)))

x_7_right_value = -((0.21/0.3)*(math.log((0.21/0.3),2))+(0.09/0.3)*(math.log((0.09/0.3),2)))

x_7_weighted_value = 0.7*x_7_left_value  + 0.3 *x_7_right_value

info_gain_x_7_value = parent_entropy_value - x_7_weighted_value

# For y <= 0.6

y_6_left_value = -((0.09 / 0.6)*(math.log((0.09 / 0.6),2))+(0.42/0.6)*(math.log((0.42/0.6),2))+(0.09/0.6)*(math.log((0.09/0.6),2)))

y_6_right_value = -((0.32/ 0.400000)*(math.log((0.32/ 0.400000),2))+(0.040/0.400000)*(math.log((0.040/0.400000),2))+(0.040/0.400000)*(math.log((0.040/0.400000),2)))

y_6_weighted_value = 0.6*y_6_left_value  + 0.400000 *y_6_right_value

info_gain_y_6_value = parent_entropy_value - y_6_weighted_value

print('x_2_left:',x_2_left_value)
print('x_2_right:',x_2_right_value)
print('x_2_weighted:',x_2_weighted_value)
print('Info_gain_x_2:',info_gain_x_2_value)
print()
print('x_7_left:',x_7_left_value)
print('x_7_right:',x_7_right_value)
print('x_7_weighted:',x_7_weighted_value)
print('Info_gain_x_7:',info_gain_x_7_value)
print()
print('y_6_left:',y_6_left_value)
print('y_6_right:',y_6_right_value)
print('y_6_weighted:',y_6_weighted_value)
print('Info_gain_y_6:',info_gain_y_6_value)

#(d)

# Root node selected x<0.7

def calculate_entropy(probabilities):
    entr = 0
    for probability in probabilities:
        if probability != 0:
            entr += probability * math.log(probability, 2)
    return -entr if entr != 0 else 0

# For y = 0.8

y_8_left_value = calculate_entropy([0.25/0.8,0.42/0.8,0.13/0.8])

y_8_right_value = calculate_entropy([0.16/0.2,0.04/0.2])

y_8_weighted_value = 0.8*y_8_left_value + 0.2*y_8_right_value

info_gain_y_8_value = parent_entropy_value - y_8_weighted_value

print('y_8_left:',y_8_left_value)
print('y_8_right:',y_8_right_value)
print('y_8_weighted:',y_8_weighted_value)
print('Info_gain_y_8:',info_gain_y_8_value)

parent_entropy_left_value = calculate_entropy([0.2/0.7,0.46/0.7,0.04/0.7])
print(parent_entropy_left_value)

# For y<0.6
y06_left_value = calculate_entropy([1])
print("Entropy for y < 0.6 (Left):", y06_left_value)
y06_right_value = calculate_entropy([0.2/0.28, 0.04/0.28, 0.04/0.28])
print("Entropy for y < 0.6 (Right):", y06_right_value)
y06_total_value = 0.42 * y06_left_value + 0.28 * y06_right_value
print("Total Entropy for y < 0.6:", y06_total_value)
info_gain_y06_value = parent_entropy_left_value - y06_total_value
print("Information Gain for y < 0.6:", info_gain_y06_value)

# For y<0.8
y08_left_value = calculate_entropy([0.42/0.56, 0.10/0.56, 0.04/0.56])
print("Entropy for y < 0.8 (Left):", y08_left_value)
y08_right_value = calculate_entropy([0.10/0.14, 0.04/0.14])
print("Entropy for y < 0.8 (Right):", y08_right_value)
y08_total_value = 0.56 * y08_left_value + 0.14 * y08_right_value
print("Total Entropy for y < 0.8:", y08_total_value)
info_gain_y08_value = parent_entropy_left_value - y08_total_value
print("Information Gain for y < 0.8:", info_gain_y08_value)

# For x<0.2
x02_left_value = calculate_entropy([0.16/0.2, 0.04/0.2])
print("Entropy for x < 0.2 (Left):", x02_left_value)
x02_right_value = calculate_entropy([0.2/0.5, 0.3/0.5])
print("Entropy for x < 0.2 (Right):", x02_right_value)
x02_total_value = 0.2 * x02_left_value + 0.5 * x02_right_value
print("Total Entropy for x < 0.2:", x02_total_value)
info_gain_x02_value = parent_entropy_left_value - x02_total_value
print("Information Gain for x < 0.2:", info_gain_x02_value)

# Calculations for right side of y<0.6
e_p_r_y06_value = calculate_entropy([0.2/0.28, 0.04/0.28, 0.04/0.28])
print("Entropy for right side of y < 0.6:", e_p_r_y06_value)

# For x<0.2
x02_left_value = calculate_entropy([0.04/0.08, 0.04/0.08])
print("Entropy for x < 0.2 (Left):", x02_left_value)
x02_right_value = calculate_entropy([0.2/0.2])
print("Entropy for x < 0.2 (Right):", x02_right_value)
x02_total_value = 0.08 * x02_left_value + 0.2 * x02_right_value
print("Total Entropy for x < 0.2:", x02_total_value)
info_gain_x02_value = e_p_r_y06_value - x02_total_value
print("Information Gain for x < 0.2:", info_gain_x02_value)

# For y<0.8
y08_left_value = calculate_entropy([0.04/0.14, 0.10/0.14])
print("Entropy for y < 0.8 (Left):", y08_left_value)
y08_right_value = calculate_entropy([0.04/0.14, 0.10/0.14])
print("Entropy for y < 0.8 (Right):", y08_right_value)
y08_total_value = 0.14 * y08_left_value + 0.14 * y08_right_value
print("Total Entropy for y < 0.8:", y08_total_value)
info_gain_y08_value = e_p_r_y06_value - y08_total_value
print("Information Gain for y < 0.8:", info_gain_y08_value)

# Right hand side of x<0.7

e_p_r1_value = calculate_entropy([0.21/0.3, 0.09/0.3])
print("Entropy for parent (Right side of tree):", e_p_r1_value)

# For y<0.6
y06_l_value = calculate_entropy([0.09/0.18, 0.09/0.18])
print("Entropy for y<0.6 (Left side):", y06_l_value)
y06_r_value = calculate_entropy([0.12/0.12])
print("Entropy for y<0.6 (Right side):", y06_r_value)
y06_value = 0.18 * y06_l_value + 0.12 * y06_r_value
print("Weighted entropy for y<0.6:", y06_value)
info_y06_value = e_p_r1_value - y06_value
print("Information Gain for y<0.6:", info_y06_value)

# For y<0.3
y03_l_value = calculate_entropy([0.09/0.09])
print("Entropy for y<0.3 (Left side):", y03_l_value)
y03_r_value = calculate_entropy([0.12/0.21, 0.09/0.21])
print("Entropy for y<0.3 (Right side):", y03_r_value)
y03_value = 0.09 * y03_l_value + 0.21 * y03_r_value
print("Weighted entropy for y<0.3:", y03_value)
info_y03_value = e_p_r1_value - y03_value
print("Information Gain for y<0.3:", info_y03_value)

print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")
print("Question 3")
"""# Question 3"""

#(a)
class_co_value = 10
class_c1_value = 10
total_instances = class_co_value + class_c1_value
p_co_value = class_co_value / total_instances
p_c1_value = class_c1_value / total_instances
gini_index_value = 1 - (p_co_value**2 + p_c1_value**2)
print(gini_index_value)

# (b)
# For each Customer ID there is no impurity , So Gini index is 0

#(c)
n_instances_value = 20
n_male_value = 10
n_female_value = 10
p_male_value = n_male_value / n_instances_value
p_female_value = n_female_value / n_instances_value
p_male_co_value = 6/n_male_value
p_male_c1_value = 4/n_male_value
p_female_co_value = 4/n_female_value
p_female_c1_value = 6/n_female_value
gini_male_value = 1 - (p_male_co_value ** 2  + p_male_c1_value ** 2)
gini_female_value = 1 - (p_female_co_value ** 2 + p_female_c1_value ** 2)
gender_gini_index_value = (p_male_value * gini_male_value) + (p_female_value * gini_female_value)
print(gender_gini_index_value)

#(d)
num_instances_value = 20
num_family_value = 4
num_sports_value = 8
num_luxury_value = 8
prob_family_value = num_family_value / num_instances_value
prob_sports_value = num_sports_value / num_instances_value
prob_luxury_value = num_luxury_value / num_instances_value
p_family_co_value = 1/num_family_value
p_family_c1_value = 3/num_family_value
p_sports_co_value = 8/num_sports_value
p_sports_c1_value = 0/num_sports_value
p_luxury_co_value = 1/num_luxury_value
p_luxury_c1_value = 7/num_luxury_value
gini_family_value = 1 - (p_family_co_value ** 2  + p_family_c1_value ** 2)
gini_sports_value = 1 - (p_sports_co_value ** 2  + p_sports_c1_value ** 2)
gini_luxury_value = 1 - (p_luxury_co_value ** 2  + p_luxury_c1_value ** 2)
overall_gini_index_value = prob_family_value * gini_family_value + prob_sports_value * gini_sports_value + prob_luxury_value * gini_luxury_value
print("Overall Gini index for Car Type (multiway split):", overall_gini_index_value)

#(e)
num_instances_value = 20
num_small_value = 5
num_medium_value = 7
num_large_value = 4
num_extra_large_value = 4

prob_small_value = num_small_value / num_instances_value
prob_medium_value = num_medium_value/ num_instances_value
prob_large_value = num_large_value / num_instances_value
prob_extra_large_value = num_extra_large_value/ num_instances_value

p_small_co_value = 3/num_small_value
p_small_c1_value = 2/num_small_value

p_medium_co_value = 3/num_medium_value
p_medium_c1_value = 4/num_medium_value

p_large_co_value = 2/num_large_value
p_large_c1_value = 2/num_large_value

p_extra_large_co_value = 2/num_extra_large_value
p_extra_large_c1_value = 2/num_extra_large_value

gini_small_value = 1 - (p_small_co_value ** 2  + p_small_c1_value ** 2)
gini_medium_value = 1 - (p_medium_co_value ** 2  + p_medium_c1_value ** 2)
gini_large_value = 1 - (p_large_co_value ** 2  + p_large_c1_value ** 2)
gini_extra_large_value = 1 - (p_extra_large_co_value ** 2  + p_extra_large_c1_value ** 2)

overall_gini_index_value = prob_small_value * gini_small_value + prob_medium_value * gini_medium_value + prob_large_value * gini_large_value + prob_extra_large_value * gini_extra_large_value

print(overall_gini_index_value)


print("----------------------------------------------------")
print("----------------------------------------------------")
print("----------------------------------------------------")


print("Question 7")
# Question 7


#a)

import math

total_items = 20
positive_items = 10
negative_items = 10

prob_positive_before = positive_items / total_items
prob_negative_before = negative_items / total_items

entropy_before = -((prob_positive_before * math.log2(prob_positive_before)) + (prob_negative_before * math.log2(prob_negative_before)))

entropy_after = 0

information_gain = entropy_before - entropy_after

print(information_gain)

#b)

import math
total_items = 20
positive_left_items = 9
negative_left_items = 1
positive_right_items = 1
negative_right_items = 9

prob_positive_before = (positive_left_items + positive_right_items) / total_items
prob_negative_before = (negative_left_items + negative_right_items) / total_items

entropy_before = -((prob_positive_before * math.log2(prob_positive_before)) + (prob_negative_before * math.log2(prob_negative_before)))

n_left = positive_left_items + negative_left_items
n_right = positive_right_items + negative_right_items
prob_left = n_left / total_items
prob_right = n_right / total_items

entropy_left = -((positive_left_items / n_left * math.log2(positive_left_items / n_left)) + (negative_left_items / n_left * math.log2(negative_left_items / n_left)))
entropy_right = -((positive_right_items / n_right * math.log2(positive_right_items / n_right)) + (negative_right_items / n_right * math.log2(negative_right_items / n_right)))

information_gain = entropy_before - (prob_left * entropy_left + prob_right * entropy_right)

print(information_gain)

#d)

import math

total_items = 20
positive_items = 10
negative_items = 10
num_unique_ids = 20

prob_positive = positive_items / total_items
prob_negative = negative_items / total_items
entropy_before_split = - (prob_positive * math.log2(prob_positive) + prob_negative * math.log2(prob_negative))


entropy_after_split_weighted_avg = 0

information_gain = entropy_before_split - entropy_after_split_weighted_avg

split_information = - sum([(1 / num_unique_ids) * math.log2(1 / num_unique_ids) for _ in range(num_unique_ids)])

gain_ratio = information_gain / split_information

print("Gain Ratio:", gain_ratio)

#e)

import math
total_items = 20
positive_left_items = 9
negative_left_items = 1
positive_right_items = 1
negative_right_items = 9

prob_positive = (positive_left_items + positive_right_items) / total_items
prob_negative = (negative_left_items + negative_right_items) / total_items
entropy_before_split = - (prob_positive * math.log2(prob_positive) + prob_negative * math.log2(prob_negative))

prob_positive_left = positive_left_items / (positive_left_items + negative_left_items)
prob_negative_left = negative_left_items / (positive_left_items + negative_left_items)
entropy_left = - (prob_positive_left * math.log2(prob_positive_left) + prob_negative_left * math.log2(prob_negative_left))

prob_positive_right = positive_right_items / (positive_right_items + negative_right_items)
prob_negative_right = negative_right_items / (positive_right_items + negative_right_items)
entropy_right = - (prob_positive_right * math.log2(prob_positive_right) + prob_negative_right * math.log2(prob_negative_right))

entropy_after_split_weighted_avg = (positive_left_items + negative_left_items) / total_items * entropy_left + (positive_right_items + negative_right_items) / total_items * entropy_right

split_information = - ((10 / 20) * math.log2(10 / 20) + (10 / 20) * math.log2(10 / 20))

information_gain = entropy_before_split - entropy_after_split_weighted_avg
gain_ratio = information_gain / split_information

print("Gain Ratio for Handedness:", gain_ratio)


print("-----------------------------------------------------------")
print("-----------------------------------------------------------")

print("Question 1")
import math

def calc_entropy(probability):
    return -probability * math.log2(probability) if probability != 0 else 0

"""## Finding out root node"""

# For smoking
yes_smoking_yes_cancer = 4 / 5
yes_smoking_no_cancer = 1 / 5
no_smoking_yes_cancer = 1 / 5
no_smoking_no_cancer = 4 / 5

# Calculate entropies
entropy_yes_smoking = calc_entropy(yes_smoking_yes_cancer) + calc_entropy(yes_smoking_no_cancer)
entropy_no_smoking = calc_entropy(no_smoking_yes_cancer) + calc_entropy(no_smoking_no_cancer)

print("Entropy for Smoking = Yes:", entropy_yes_smoking)
print("Entropy for Smoking = No:", entropy_no_smoking)
print("----------------------------------------------------")
parent_entropy = calc_entropy(5/10) + calc_entropy(5/10)

information_gain = 1 - ((5/10) * entropy_yes_smoking + (5/10) * entropy_no_smoking)

print("Information Gain:", information_gain)
print("----------------------------------------------------")
# For Radon
yes_radon_yes_cancer = 2/2
yes_radon_no_cancer = 0/2
no_radon_yes_cancer = 3/8
no_radon_no_cancer = 5 / 8

# Calculate entropies
entropy_yes_radon = calc_entropy(yes_radon_yes_cancer) + calc_entropy(yes_radon_no_cancer)
entropy_no_radon = calc_entropy(no_radon_yes_cancer) + calc_entropy(no_radon_no_cancer)

print("Entropy for radon = Yes:", entropy_yes_radon)
print("Entropy for radon = No:", entropy_no_radon)
print("----------------------------------------------------")
parent_entropy = calc_entropy(5/10) + calc_entropy(5/10)


information_gain_radon = parent_entropy - ((2/10) * entropy_yes_radon + (8/10) * entropy_no_radon)

print("Information Gain for Radon:", information_gain_radon)
print("----------------------------------------------------")
# For Chronic Cough
yes_cough_yes_cancer = 4/7
yes_cough_no_cancer = 3/7
no_cough_yes_cancer = 1/3
no_cough_no_cancer = 2/3

# Calculate entropies
entropy_yes_cough = calc_entropy(yes_cough_yes_cancer) + calc_entropy(yes_cough_no_cancer)
entropy_no_cough = calc_entropy(no_cough_yes_cancer) + calc_entropy(no_cough_no_cancer)

print("Entropy for cough = Yes:", entropy_yes_cough)
print("Entropy for cough = No:", entropy_no_cough)
print("----------------------------------------------------")
parent_entropy = calc_entropy(5/10) + calc_entropy(5/10)


information_gain_cough = parent_entropy - ((7/10) * entropy_yes_cough + (3/10) * entropy_no_cough)

print("Information Gain for cough:", information_gain_cough)
print("----------------------------------------------------")
# For Weight Loss
yes_Weight_yes_cancer = 3/5
yes_Weight_no_cancer = 2/5
no_Weight_yes_cancer = 2/5
no_Weight_no_cancer = 3/5

# Calculate entropies
entropy_yes_Weight = calc_entropy(yes_Weight_yes_cancer) + calc_entropy(yes_Weight_no_cancer)
entropy_no_Weight = calc_entropy(no_Weight_yes_cancer) + calc_entropy(no_Weight_no_cancer)

print("Entropy for Weight = Yes:", entropy_yes_Weight)
print("Entropy for Weight = No:", entropy_no_Weight)
print("----------------------------------------------------")
parent_entropy = calc_entropy(5/10) + calc_entropy(5/10)


information_gain_Weight = parent_entropy - ((5/10) * entropy_yes_Weight + (5/10) * entropy_no_Weight)

print("Information Gain for Weight:", information_gain_Weight)

print("Information Gain for Smoking:", information_gain)
print("Information Gain for Radon:", information_gain_radon)
print("Information Gain for cough:", information_gain_cough)
print("Information Gain for Weight:", information_gain_Weight)
print("----------------------------------------------------")
print("----------------------------------------------------")

"""## Considering Smoking as root node and moving to next level

## For Smoking = Yes
"""

# For Radon
yes_radon_yes_cancer = 1/1
yes_radon_no_cancer = 0/1
no_radon_yes_cancer = 3/4
no_radon_no_cancer = 1/4

# Calculate entropies
entropy_yes_radon = calc_entropy(yes_radon_yes_cancer) + calc_entropy(yes_radon_no_cancer)
entropy_no_radon = calc_entropy(no_radon_yes_cancer) + calc_entropy(no_radon_no_cancer)

print("Entropy for radon = Yes:", entropy_yes_radon)
print("Entropy for radon = No:", entropy_no_radon)
print("----------------------------------------------------")
parent_entropy = calc_entropy(4/5) + calc_entropy(1/5)

information_gain_radon = parent_entropy - ((1/5) * entropy_yes_radon + (4/5) * entropy_no_radon)

print("Information Gain for Radon:", information_gain_radon)
print("----------------------------------------------------")
# For Chronic Cough
yes_cough_yes_cancer = 4/4
yes_cough_no_cancer = 0/4
no_cough_yes_cancer = 0/1
no_cough_no_cancer = 1/1

# Calculate entropies
entropy_yes_cough = calc_entropy(yes_cough_yes_cancer) + calc_entropy(yes_cough_no_cancer)
entropy_no_cough = calc_entropy(no_cough_yes_cancer) + calc_entropy(no_cough_no_cancer)

print("Entropy for cough = Yes:", entropy_yes_cough)
print("Entropy for cough = No:", entropy_no_cough)
print("----------------------------------------------------")
parent_entropy = calc_entropy(4/5) + calc_entropy(1/5)

information_gain_cough = parent_entropy - ((4/5) * entropy_yes_cough + (1/5) * entropy_no_cough)

print("Information Gain for Radon:", information_gain_cough)
print("----------------------------------------------------")
# For Weight Loss
yes_Weight_yes_cancer = 2/2
yes_Weight_no_cancer = 0/2
no_Weight_yes_cancer = 2/3
no_Weight_no_cancer = 1/3

# Calculate entropies
entropy_yes_Weight = calc_entropy(yes_Weight_yes_cancer) + calc_entropy(yes_Weight_no_cancer)
entropy_no_Weight = calc_entropy(no_Weight_yes_cancer) + calc_entropy(no_Weight_no_cancer)

print("Entropy for Weight = Yes:", entropy_yes_Weight)
print("Entropy for Weight = No:", entropy_no_Weight)
print("----------------------------------------------------")
parent_entropy = calc_entropy(4/5) + calc_entropy(1/5)


information_gain_Weight = parent_entropy - ((2/5) * entropy_yes_Weight + (3/5) * entropy_no_Weight)
print("----------------------------------------------------")
print("Information Gain for Weight:", information_gain_Weight)

print("Information Gain for Radon:", information_gain_radon)
print("Information Gain for cough:", information_gain_cough)
print("Information Gain for Weight:", information_gain_Weight)

"""## For Smoking = No"""

# For Radon
yes_radon_yes_cancer = 1/1
yes_radon_no_cancer = 0/1
no_radon_yes_cancer = 0/4
no_radon_no_cancer = 4/4

# Calculate entropies
entropy_yes_radon = calc_entropy(yes_radon_yes_cancer) + calc_entropy(yes_radon_no_cancer)
entropy_no_radon = calc_entropy(no_radon_yes_cancer) + calc_entropy(no_radon_no_cancer)

print("Entropy for radon = Yes:", entropy_yes_radon)
print("Entropy for radon = No:", entropy_no_radon)
print("----------------------------------------------------")
parent_entropy = calc_entropy(4/5) + calc_entropy(1/5)

information_gain_radon = parent_entropy - ((1/5) * entropy_yes_radon + (4/5) * entropy_no_radon)

print("Information Gain for Radon:", information_gain_radon)
print("----------------------------------------------------")
# For Weight Loss
yes_Weight_yes_cancer = 1/3
yes_Weight_no_cancer = 2/3
no_Weight_yes_cancer = 0/2
no_Weight_no_cancer = 2/2

# Calculate entropies
entropy_yes_Weight = calc_entropy(yes_Weight_yes_cancer) + calc_entropy(yes_Weight_no_cancer)
entropy_no_Weight = calc_entropy(no_Weight_yes_cancer) + calc_entropy(no_Weight_no_cancer)

print("Entropy for Weight = Yes:", entropy_yes_Weight)
print("Entropy for Weight = No:", entropy_no_Weight)
print("----------------------------------------------------")
parent_entropy = calc_entropy(4/5) + calc_entropy(1/5)


information_gain_Weight = parent_entropy - ((3/5) * entropy_yes_Weight + (2/5) * entropy_no_Weight)

print("Information Gain for Weight:", information_gain_Weight)

print("Information Gain for Radon:", information_gain_radon)
print("Information Gain for Weight:", information_gain_Weight)
print("----------------------------------------------------")
"""## Training error"""

Samples = 10
Misclassfication = 0
Training_error = Misclassfication/Samples
print(Training_error)

