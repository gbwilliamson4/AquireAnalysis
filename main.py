import streamlit as st
from Players import Players
from Tier1 import Tower, Luxor
from Tier2 import American, Worldwide, Festival
from Tier3 import Imperial, Continental
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
# Setup back end objects
player_list = []
P1 = Players("P1", 1)
P2 = Players("P2", 2)
P3 = Players("P3", 3)
P4 = Players("P4", 4)

player_list.append(P1)
player_list.append(P2)
player_list.append(P3)
player_list.append(P4)

# Tier 1 eompanies
Tower = Tower()
Luxor = Luxor()

# Tier 2 companies
American = American()
Worldwide = Worldwide()
Festival = Festival()

# Tier 3 companies
Imperial = Imperial()
Continental = Continental()


def update_companies():
    # Tier 1
    Tower.value_update()
    Luxor.value_update()

    # Tier 2
    American.value_update()
    Worldwide.value_update()
    Festival.value_update()

    # Tier 3
    Imperial.value_update()
    Continental.value_update()


# -------- Start web design here --------
st.title("George's Aquire Test")
# Setup display of web
# Display number of company squares at the very top, then have everything else split into columns
# American.squares = st.number_input("Current American Squares", 0, 100)
# Worldwide.squares = st.number_input("Current Worldwide Squares", 0, 100)
# Festival.squares = st.number_input("Current Festival Squares", 0, 100)

st.subheader("Tier 1 Companies")
col1, col2 = st.columns((1, 1))
with col1:
    Tower.squares = st.number_input("Current American Squares", 0, 100, key=11)

with col2:
    Luxor.squares = st.number_input("Current Luxor Squares", 0, 100, key=12)

st.subheader("Tier 2 Companies")
col1, col2, col3 = st.columns((1, 1, 1))
with col1:
    American.squares = st.number_input("Current American Squares", 0, 100, key=21)
with col2:
    Worldwide.squares = st.number_input("Current Worldwide Squares", 0, 100, key=22)
with col3:
    Festival.squares = st.number_input("Current Festival Squares", 0, 100, key=23)

st.subheader("Tier 3 Companies")
col1, col2 = st.columns((1, 1))
with col1:
    Imperial.squares = st.number_input("Current Imperial Squares", 0, 100, key=31)

with col2:
    Continental.squares = st.number_input("Current Continental Squares", 0, 100, key=32)

st.subheader("Player Info Tracking")
col1, col2, col3, col4 = st.columns((1, 1, 1, 1))

update_companies()

with col1:
    P1.player_name = st.text_input(P1.player_name, key=P1.key)

    P1.tower_holdings = st.number_input(f"Tower Shares", 0, 10, key=111)
    P1.luxor_holdings = st.number_input(f"Luxor Shares", 0, 10, key=112)

    P1.american_holdings = st.number_input(f"American Shares", 0, 10, key=113)
    P1.worldwide_holdings = st.number_input(f"Worldwide Shares", 0, 10, key=114)
    P1.festival_holdings = st.number_input(f"Festival Shares", 0, 10, key=115)

    P1.imperial_holdings = st.number_input(f"Imperial Shares", 0, 10, key=116)
    P1.continental_holdings = st.number_input(f"Continental Shares", 0, 10, key=117)

    # st.write(f"{P1.player_name} currently has ${P1.american_holdings * American.vps} worth of American")
    # st.write(f"{P1.player_name} currently has ${P1.worldwide_holdings * Worldwide.vps} worth of Worldwide")

with col2:
    P2.player_name = st.text_input(P2.player_name, key=P2.key)

    P2.tower_holdings = st.number_input(f"Tower Shares", 0, 10, key=221)
    P2.luxor_holdings = st.number_input(f"Luxor Shares", 0, 10, key=222)

    P2.american_holdings = st.number_input(f"American Shares", 0, 10, key=223)
    P2.worldwide_holdings = st.number_input(f"Worldwide Shares", 0, 10, key=224)
    P2.festival_holdings = st.number_input(f"Festival Shares", 0, 10, key=225)

    P2.imperial_holdings = st.number_input(f"Imperial Shares", 0, 10, key=226)
    P2.continental_holdings = st.number_input(f"Continental Shares", 0, 10, key=227)

with col3:
    P3.player_name = st.text_input(P3.player_name, key=P3.key)

    P3.tower_holdings = st.number_input(f"Tower Shares", 0, 10, key=331)
    P3.luxor_holdings = st.number_input(f"Luxor Shares", 0, 10, key=332)

    P3.american_holdings = st.number_input(f"American Shares", 0, 10, key=333)
    P3.worldwide_holdings = st.number_input(f"Worldwide Shares", 0, 10, key=334)
    P3.festival_holdings = st.number_input(f"Festival Shares", 0, 10, key=335)

    P3.imperial_holdings = st.number_input(f"Imperial Shares", 0, 10, key=336)
    P3.continental_holdings = st.number_input(f"Continental Shares", 0, 10, key=337)

with col4:
    P4.player_name = st.text_input(P4.player_name, key=P4.key)

    P4.tower_holdings = st.number_input(f"Tower Shares", 0, 10, key=441)
    P4.luxor_holdings = st.number_input(f"Luxor Shares", 0, 10, key=442)

    P4.american_holdings = st.number_input(f"American Shares", 0, 10, key=443)
    P4.worldwide_holdings = st.number_input(f"Worldwide Shares", 0, 10, key=444)
    P4.festival_holdings = st.number_input(f"Festival Shares", 0, 10, key=445)

    P4.imperial_holdings = st.number_input(f"Imperial Shares", 0, 10, key=446)
    P4.continental_holdings = st.number_input(f"Continental Shares", 0, 10, key=447)

st.header("Analysis")

col1, col2, col3, col4 = st.columns((1, 1, 1, 1))
with col1:
    st.write("this is the first column")

with col2:
    st.write("this is the second column")

with col3:
    st.write("this is the third column")

with col4:
    st.write("this is the fourth column")

# if st.button('stuff'):
#     st.write("The button has been pressed")
#     for player in player_list:
#         update_companies()
#         # print(player.player_name)
#         st.write(f"{player.player_name} currently has {player.american_holdings} shares of American.")
#         st.write(f"There are currently {American.squares} out on the market.")
#         st.write(f"American is currently valued at {American.vps}")
#         st.write(f"{player.player_name} currently has ${American.vps * player.american_holdings} worth of American.")

# Trying to figure out the graph

d = {'Index Title': ["Tower", "Luxor", "American", "Worldwide", "Festival", "Imperial", "Continental"]}

P1_vps = []
P1_vps.append(P1.tower_holdings * Tower.vps)
P1_vps.append(P1.luxor_holdings * Luxor.vps)
P1_vps.append(P1.american_holdings * American.vps)
P1_vps.append(P1.worldwide_holdings * Worldwide.vps)
P1_vps.append(P1.festival_holdings * Festival.vps)
P1_vps.append(P1.imperial_holdings * Imperial.vps)
P1_vps.append(P1.continental_holdings * Continental.vps)

P2_vps = []
P2_vps.append(P2.tower_holdings * Tower.vps)
P2_vps.append(P2.luxor_holdings * Luxor.vps)
P2_vps.append(P2.american_holdings * American.vps)
P2_vps.append(P2.worldwide_holdings * Worldwide.vps)
P2_vps.append(P2.festival_holdings * Festival.vps)
P2_vps.append(P2.imperial_holdings * Imperial.vps)
P2_vps.append(P2.continental_holdings * Continental.vps)

P3_vps = []
P3_vps.append(P3.tower_holdings * Tower.vps)
P3_vps.append(P3.luxor_holdings * Luxor.vps)
P3_vps.append(P3.american_holdings * American.vps)
P3_vps.append(P3.worldwide_holdings * Worldwide.vps)
P3_vps.append(P3.festival_holdings * Festival.vps)
P3_vps.append(P3.imperial_holdings * Imperial.vps)
P3_vps.append(P3.continental_holdings * Continental.vps)

P4_vps = []
P4_vps.append(P4.tower_holdings * Tower.vps)
P4_vps.append(P4.luxor_holdings * Luxor.vps)
P4_vps.append(P4.american_holdings * American.vps)
P4_vps.append(P4.worldwide_holdings * Worldwide.vps)
P4_vps.append(P4.festival_holdings * Festival.vps)
P4_vps.append(P4.imperial_holdings * Imperial.vps)
P4_vps.append(P4.continental_holdings * Continental.vps)

col1, col2 = st.columns((1, 1))

with col1:
    df = pd.DataFrame({P1.player_name: P1_vps,
                       P2.player_name: P2_vps,
                       P3.player_name: P3_vps,
                       P4.player_name: P4_vps},
                      index=["Tower", "Luxor", "American", "Worldwide", "Festival", "Imperial", "Continental"])
    total = df.sum()
    total.name = 'Total'
    df = df.append(total.transpose())
    st.write(df)

with col2:
    pass
    # Shareholder bonuses will go in this table