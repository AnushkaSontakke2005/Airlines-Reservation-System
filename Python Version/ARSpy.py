import streamlit as st
import pandas as pd

# Initialize session state
if 'passengers' not in st.session_state:
    st.session_state.passengers = []
if 'seat_map' not in st.session_state:
    st.session_state.seat_map = [0] * 100  # 0: available, 1: booked
if 'reservation_counter' not in st.session_state:
    st.session_state.reservation_counter = 1000

def book_ticket():
    st.header("Book Your Flight Ticket")

    fname = st.text_input("First Name")
    lname = st.text_input("Last Name")
    ID = st.text_input("ID")
    phone = st.text_input("Phone Number")

    st.subheader("Flight Route")
    cities = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Hyderabad"]
    source = st.selectbox("Source", cities, index=0)
    destination = st.selectbox("Destination", cities, index=1)

    if source == destination:
        st.warning("Source and destination cannot be the same.")
        return

    st.subheader("Select a Seat")
    available_seats = [i + 1 for i, s in enumerate(st.session_state.seat_map) if s == 0]
    seat = st.selectbox("Available Seats", available_seats)

    food = st.radio("Food Preference", ["Veg", "Non-Veg", "No Food"])

    if st.button("Book Ticket"):
        # Save booking
        st.session_state.seat_map[seat - 1] = 1
        st.session_state.reservation_counter += 1

        passenger = {
            "Reservation Number": st.session_state.reservation_counter,
            "First Name": fname,
            "Last Name": lname,
            "ID": ID,
            "Phone": phone,
            "Seat Number": seat,
            "Food": food
        }
        st.session_state.passengers.append(passenger)

        st.success(f"Ticket booked successfully! Reservation Number: {st.session_state.reservation_counter}")

def cancel_ticket():
    st.header("Cancel Your Ticket")
    res_number = st.number_input("Enter your reservation number", step=1, format="%d")
    if st.button("Cancel"):
        found = False
        for p in st.session_state.passengers:
            if p["Reservation Number"] == res_number:
                st.session_state.seat_map[p["Seat Number"] - 1] = 0
                st.session_state.passengers.remove(p)
                st.success("Ticket cancelled successfully.")
                found = True
                break
        if not found:
            st.error("Reservation not found.")

def change_reservation():
    st.header("Change Reservation")
    res_number = st.number_input("Enter your reservation number", step=1, format="%d")
    passenger = next((p for p in st.session_state.passengers if p["Reservation Number"] == res_number), None)
    if passenger:
        st.info(f"Current seat: {passenger['Seat Number']}")
        available_seats = [i + 1 for i, s in enumerate(st.session_state.seat_map) if s == 0]
        new_seat = st.selectbox("Choose a new seat", available_seats)

        if st.button("Change Seat"):
            st.session_state.seat_map[passenger["Seat Number"] - 1] = 0
            st.session_state.seat_map[new_seat - 1] = 1
            passenger["Seat Number"] = new_seat
            st.success("Seat changed successfully!")
    else:
        st.warning("Reservation not found.")

def view_passenger():
    st.header("Passenger Details")
    res_number = st.number_input("Enter your reservation number", step=1, format="%d")
    passenger = next((p for p in st.session_state.passengers if p["Reservation Number"] == res_number), None)
    if passenger:
        st.table(pd.DataFrame([passenger]))
    else:
        st.warning("Reservation not found.")

def view_all_bookings():
    st.header("All Booking Details")
    if st.session_state.passengers:
        st.dataframe(pd.DataFrame(st.session_state.passengers))
    else:
        st.info("No bookings yet.")

def seat_map_view():
    st.header("Seat Map")
    cols = st.columns(10)
    for i in range(100):
        with cols[i % 10]:
            label = f"{i+1}"
            color = "green" if st.session_state.seat_map[i] == 0 else "red"
            st.markdown(f"<div style='text-align:center;background-color:{color};color:white;border-radius:4px;padding:4px'>{label}</div>", unsafe_allow_html=True)

# Streamlit UI Menu
st.title("✈️ Airline Reservation System")

st.sidebar.markdown("## ✈️ **Main Menu**", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Select an Option:",
    [
        "Book Ticket",
        "Cancel Ticket",
        "Change Reservation",
        "Passenger Details",
        "View All Bookings",
        "View Seat Map"
    ]
)

if menu == "Book Ticket":
    book_ticket()
elif menu == "Cancel Ticket":
    cancel_ticket()
elif menu == "Change Reservation":
    change_reservation()
elif menu == "Passenger Details":
    view_passenger()
elif menu == "View All Bookings":
    view_all_bookings()
elif menu == "View Seat Map":
    seat_map_view()
