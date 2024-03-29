import latex.latex as lx

content_dictionary = {
    1: {"media": "./static/RightTriangleWithDots.png",
        "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters.  Assume sin(30 degrees) is .5, cos(60 degrees) is .5 and tan(37 degrees) is .75.  What is the arctan of the blue side over the green side (in degrees)?",
        "options": ["30", "45", "60","37"],
        "answer": "37",
        "explanation": "The tan(A) is 6/8 or 3/4 or .75.  Thus if tan(37) is .75, then arctan is 37 degrees."},
    2: {"media": "./static/RightTriangleWithDots.png",
        "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters.  What is the secant of angle A?",
        "options": ["1", "1.25", "1.33", "8/12"],
        "answer": "1.25",
        "explanation": "The cos(A) = 8/10 = 4/5 so the secant 1/4/5 = 5/4 = 1.25."},
    3: {"media": "./static/RightTriangleWithDots.png",
        "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters.  Assume sin(53 deg.) is .8.  Assume cos(53 deg.) is .60.  Assume tan(30 deg.) is .58.  What is the arcsin of the green side over the hypotenuse?",
        "options": ["30", "60", "53", "Undefined"],
        "answer": "53",
        "explanation": "The sin(B) = 8/10 or 4/5 or .8.  So arcsin(.8) is 53 degrees"},
    4: {"media": "./static/RightTriangleWithDots.png",
        "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters.  What is the cotangent of the right angle?",
        "options": ["0", "1", "Undefined", "3"],
        "answer": "Undefined",
        "explanation": "The tan(90) = 0 and 1/0 is undefined."},
    5: {"media": "./static/RightTriangleWithDots.png",
        "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters.  What is the cosine of the right angle?",
        "options": ["1", "0", "8/10", "6/10"],
        "answer": "0",
        "explanation": "The cosine(C) = adjacent over hypotenuse.  Since there is no single adjacent side, this is equal to 0/10 or 0."},
    6: {"media": "./static/RightTriangleWithDots.png",
        "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters.  What is the cotangent of angle A?",
        "options": ["8/6", "6/8", "4/5", "2/3"],
        "answer": "8/6",
        "explanation": "The tan(A) is 6/8 so the cot(A) is 8/6."},
    7: {"media": "./static/RightTriangleWithDots.png",
        "question": "If the secant of 30 degrees is 2, then what is the arcsecant of 2?",
        "options": ["60 degrees", "90 degrees", "30 degrees", "10 degrees"],
        "answer": "30 degrees",
        "explanation": "Remember arc just means to take the inverse of the function so instead of feeding the function 30 degrees and getting 2 back you feed 2 to the function and get 30 degrees back."},
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
    10: {"media": "./static/RightTriangleWithDots.png",
         "question": "Assume the blue:blue side is 6 meters, the green:green side is 8 meters, and the red:red side is 10 meters. What is the secant of the angle at B?",
         "options": ["10/8", ".7", "1", ".5"],
         "answer": "10/8",
         "explanation": "The cosine of the angle at B is 8/10 and secant is 1/cos so the answer is 10/8."},
}
