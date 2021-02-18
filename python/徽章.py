import turtle
chinese_score = turtle.numinput("成绩单","语文")

math_score = turtle.numinput("成绩单","数学")

english_score = turtle.numinput("成绩单","英语")

print("语文：",chinese_score)

print("数学：",math_score)

print("英语：",english_score)

if chinese_score > 90 and math_score > 90 and english_score > 90:
    print("获得荣誉胸章")
    pen = turtle.Pen()
    pen.dot(100,"gold")
    pen.dot(90,"orange")
    pen.dot(80,"gold")
    pen.dot(70, "orange")
    pen.penup()
    pen.goto(0,10)
    pen.fillcolor("red")
    pen.shape("turtle")
    pen.stamp()
    pen.goto(-17,-17)
    pen.write("优秀训练师")
    pen.hideturtle()
    turtle.done()
elif chinese_score < 60 or math_score < 60 or english_score < 60:
    print("别灰心，下次努力")
else:
    print("再接再厉")
