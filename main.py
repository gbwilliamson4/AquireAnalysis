import streamlit as st
from Players import Players
from American import American

st.title("George's Aquire Test")
player_list = []
P1 = Players()


American = American()

# Create and add players to list.
for i in range(int(st.slider("Players", 2, 5))):
    player_list.append(Players(st.text_input(f'Player {i}')))

# Assign key values to each player to avoid errors when forms are loading.
for i in range(len(player_list)):
    player_list[i].key = i

for player in player_list:
    player.holdings = st.number_input(f"American holdings for {player.player_name}.", 0, 100, key=player.key)
    print(player.holdings)

American.squares = st.number_input("Current American Squares", 0, 100)

if st.button('stuff'):
    st.write("The button has been pressed")
    for player in player_list:
        American.value_update()
        # print(player.player_name)
        st.write(f"{player.player_name} currently has {player.holdings} shares of American.")
        st.write(f"There are currently {American.squares} out on the market.")
        st.write(f"American is currently valued at {American.vps}")
        st.write(f"{player.player_name} currently has ${American.vps * player.holdings} worth of American.")

col1, col2, col3, col4 = st.columns((1, 1, 1, 1))

with col1:
    st.number_input("Col1", 0, 10)

with col2:
    st.number_input("Col2", 0, 10)

with col3:
    st.number_input("Col3", 0, 10)

with col4:
    st.number_input("Col4", 0, 10)
