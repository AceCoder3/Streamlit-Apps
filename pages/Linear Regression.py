import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

StudyTime=[50,75,80,90,95,100]
Grade=[59,61,65,69,72,77]

data=pd.DataFrame({"StudyTime" : StudyTime, "Grade" : Grade})
st.dataframe(data)

Model=LinearRegression()
Model.fit(data[["StudyTime"]],data["Grade"])

m=Model.coef_[0]
b=Model.intercept_
y= lambda x : m*x + b

predict=[]

for i in StudyTime:
    predict.append(y(i))

future_studytime=[110,120,130,140]
future_Grade=[y(i) for i in future_studytime]

fig = plt.figure(figsize=(3, 3))
plt.scatter(StudyTime,Grade , color="purple"),
plt.plot(StudyTime,Grade),
plt.plot(StudyTime,Grade),
plt.plot(future_studytime,future_Grade),
plt.title("Grades in Percentages compared to study time in minutes"),
plt.xlabel("Study Time"),
plt.ylabel("Grade")

st.pyplot(fig)

a=st.number_input("How Long Do you study?")

st.caption(f"You should expect a grade of {y(a)}")




