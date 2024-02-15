# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] = 0.2781

    level1["cough"] = -1.0
    level1["cough_info_gain"] = 0.2365

    level1["radon"] = -1.0
    level1["radon_info_gain"] = 0.0350

    level1["weight_loss"] = -1.0
    level1["weight_loss_info_gain"] = 0.0291

    level2_left["smoking"] = -1.0
    level2_left["smoking_info_gain"] = 0.0
    level2_right["smoking"] = -1.0
    level2_right["smoking_info_gain"] = 0.0

    level2_left["radon"] = -1.0
    level2_left["radon_info_gain"] = 0.0729

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.7219

    level2_left["weight_loss"] = -1.0
    level2_left["weight_loss_info_gain"] = 0.1710

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] = 0.7219

    level2_right["cough"] = -1.0
    level2_right["cough_info_gain"] = 0.3219

    level2_right["weight_loss"] = -1.0
    level2_right["weight_loss_info_gain"] = 0.1711

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("smoking")  # MUST STILL CREATE THE TREE *****
    A = tree.insert_left("cough")
    B = tree.insert_right("radon")
    A.insert_left("Yes")
    A.insert_right("No")
    B.insert_left("Yes")
    B.insert_right("No")  # MUST STILL CREATE THE TREE *****
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 0.
    # Infogain
    answer["(b) x <= 0.2"] = 0.
    answer["(b) x <= 0.7"] = 0.
    answer["(b) y <= 0.6"] = 0.

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = ""  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("Root")
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1622
    answer["(e) Gini, Shirt type"] = 0.4914

    answer["(f) attr for splitting"] = "Car type"

    # Explanatory text string
    answer["(f) explain choice"] = "Car type has the least gini value"

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ['binary','qualitative','ordinal']

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = ""

    answer["b"] = ['continuous','quantitative','ratio']
    answer["b: explain"] = ""

    answer["c"] = ['discrete','qualitative','ordinal']
    answer["c: explain"] = ""

    answer["d"] = ['continuous','quantitative','ratio']
    answer["d: explain"] = ""

    answer["e"] = ['discrete','qualitative','ordinal']
    answer["e: explain"] = ""

    answer["f"] = ['continuous','quantitative','interval']
    answer["f: explain"] = ""

    answer["g"] = ['discrete','quantitative','ratio']
    answer["g: explain"] = ""

    answer["h"] = ['discrete','qualitative','nominal']
    answer["h: explain"] = ""

    answer["i"] = ['discrete','qualitative','ordinal']
    answer["i: explain"] = ""

    answer["j"] = ['discrete','qualitative','ordinal']
    answer["j: explain"] = ""

    answer["k"] = ['continuous','quantitative','ratio']
    answer["k: explain"] = ""

    answer["l"] = ['continuous','quantitative','ratio']
    answer["l: explain"] = ""

    answer["m"] = ['discrete','qualitative','nominal']
    answer["m: explain"] = ""

    return answer


# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Model 1 has high accuracy on A but lower accuracy on B, indicating overfitting; whereas, Model 2's accuracy on both datasets A and B is nearly same, indicating superior generalization to new data. "

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "Despite a minor loss in accuracy, Model 2 is still superior due to improved generalization and a lower likelihood of overfitting."

    explain["c similarity"] = "Penalty on Complexity / Regularization"
    explain["c similarity explain"] = "They are similar, since they penalize the complexity of the model"

    explain["c difference"] = ""
    explain["c difference explain"] = ""

    return explain


# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = ""
    answer["a, level 2, right"] =""
    answer["a, level 2, left"] = ""
    answer["a, level 3, left"] = ""
    answer["a, level 3, right"] = ""

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("root note")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.531

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.2314
    answer["e, gain ratio, Handedness"] = 0.531

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

