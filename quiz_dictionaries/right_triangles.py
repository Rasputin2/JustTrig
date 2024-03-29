import latex.latex as lx

content_dictionary = {
    1: {"media": "./static/RightTriangleWithDots.png",
          "question": "What is a right angle?",
          "options": ["A triangle with a 90 degree angle.", "A right triangle.", "An angle equaling 90 degrees.",
                      "An angle equal to 3/4 pi radians."],
          "answer": "An angle equaling 90 degrees.",
          "explanation": "The answer is an angle equaling 90 degrees."},
    2: {"media": "./static/RightTriangleWithDots.png",
          "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters.  What is the sine of angle A?",
          "options": ["6", "6/8", "3/5", "8/10"],
          "answer": "3/5",
          "explanation": "The sin(A) = 6/10 or 3/5."},
    3: {"media": "./static/RightTriangleWithDots.png",
          "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters.  What is the sine of angle B?",
          "options": ["1", "8/6", "4/5", "6/8"],
          "answer": "4/5",
          "explanation": "The sin(B) = 8/10 or 4/5."},
    4: {"media": "./static/RightTriangleWithDots.png",
          "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters.  What is the sine of the right angle?",
          "options": ["1", "8/10", "10/8", "6/10"],
          "answer": "1",
          "explanation": "The sine(C) = sin(90) = hypotenuse/hypotenuse = 10/10 or 1."},
    5: {"media": "./static/RightTriangleWithDots.png",
          "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters.  What is the cosine of the right angle?",
          "options": ["1", "0", "8/10", "6/10"],
          "answer": "0",
          "explanation": "The cosine(C) = adjacent over hypotenuse.  Since there is no adjacent side, this is equal to 0/10 or 0."},
    6: {"media": "./static/RightTriangleWithDots.png",
          "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters.  What is the cosine of angle A?",
          "options": ["8/6", "6/8", "4/5", "2/3"],
          "answer": "4/5",
          "explanation": "The cosine is adjacent over hypotenuse which is 8/10 or 4/5."},
    7: {"media": "./static/RightTriangleWithDots.png",
          "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters. What is the cosine of angle B?",
          "options": ["3/5", "6/8", "8/10", "undefined"],
          "answer": "3/5",
          "explanation": "Cosine of B = 8/10 or 4/5."},
    8: {"media": "./static/RightTriangleWithDots.png",
          "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters. What is the tangent of angle C?",
          "options": ["undefined", "1", "0", "6/8"],
          "answer": "undefined",
          "explanation": "Tangent(C) = opposite / adjacent = 10/0 which is undefined."},
    9: {"media": "./static/RightTriangleWithDots.png",
          "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters. What is the tangent of angle B?",
          "options": ["4/3", "3/4", "5/4", "1"],
          "answer": "4/3",
          "explanation": "The tangent(B) is 8/6 = 4/3."},
    10: {  "media": "./static/EquilateralTriangle.png",
           "question": "Assume each side of this equilateral triangle has a length of 6.  Based solely on this information, can you determine the sine of 30 degrees?",
           "options": [".2", ".7", "1", ".5"],
           "answer": ".5",
           "explanation": "This is tricky.  First, drop a perpendicular from the topmost angle to the base of the triangle.  By dividing that top angle in half you know the angle on either side is 30 degrees. Now, you have split the single equilateral triangle into two right triangles, each with angles 30, 60, 90.  You know the length of the hypotenuse is 6.  You know the side opposite the 30 degree angle is 3 (1/2 of 6).  Sine(30) = opposite/hypotenuse = 3/6 = .5."},
}
