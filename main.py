import streamlit as st
from Players import Players
from American import American

st.title("George's Aquire Test")

# Setup player objects
player_list = []
P1 = Players("P1")
P2 = Players("P2")
P3 = Players("P3")
P4 = Players("P4")

player_list.append(P1)
player_list.append(P2)
player_list.append(P3)
player_list.append(P4)

American = American()

# Setup display of web
# Display number of company squares at the very top, then have everything else split into columns
American.squares = st.number_input("Current American Squares", 0, 100)
American.value_update()

col1, col2, col3, col4 = st.columns((1, 1, 1, 1))
with col1:
    P1.player_name = st.text_input(P1.player_name)
    P1.american_holdings = st.number_input(f"American Shares for {P1.player_name}", 0, 10)
    st.write(f"{P1.player_name} currently has ${P1.american_holdings * American.vps} worth of American")


with col2:
    P2.player_name = st.text_input(P2.player_name)
    P2.american_holdings = st.number_input(f"American Shares for {P2.player_name}", 0, 10)
    st.write(f"{P2.player_name} currently has ${P2.american_holdings * American.vps} worth of American")


with col3:
    P3.player_name = st.text_input(P3.player_name)
    P3.american_holdings = st.number_input(f"American Shares for {P3.player_name}", 0, 10)
    st.write(f"{P3.player_name} currently has ${P3.american_holdings * American.vps} worth of American")


with col4:
    P4.player_name = st.text_input(P4.player_name)
    P4.american_holdings = st.number_input(f"American Shares for {P4.player_name}", 0, 10)
    st.write(f"{P4.player_name} currently has ${P4.american_holdings * American.vps} worth of American")




if st.button('stuff'):
    st.write("The button has been pressed")
    for player in player_list:
        American.value_update()
        # print(player.player_name)
        st.write(f"{player.player_name} currently has {player.american_holdings} shares of American.")
        st.write(f"There are currently {American.squares} out on the market.")
        st.write(f"American is currently valued at {American.vps}")
        st.write(f"{player.player_name} currently has ${American.vps * player.american_holdings} worth of American.")


