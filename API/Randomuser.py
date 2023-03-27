from randomuser import RandomUser
import os
import pandas as pd


def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        users.append({"Name": user.get_full_name(), "Gender": user.get_gender(), "City": user.get_city(),
                      "State": user.get_state(), "DOB": user.get_dob(),
                      "Picture": user.get_picture()})

    return pd.DataFrame(users)

df1 = pd.DataFrame(get_users())
print(df1)
df2 = df1.to_excel('RandomUser.xlsx')