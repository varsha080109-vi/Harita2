import streamlit as st
import pandas as pd

st.title("📞 Contact Management System")

# Store contacts
if "contacts" not in st.session_state:
    st.session_state.contacts = []

# Menu
menu = st.sidebar.selectbox(
    "Select Option",
    ["Add Contact", "View Contacts",
     "Search Contact", "Update Contact", "Delete Contact"]
)

# Add Contact
if menu == "Add Contact":

    st.header("Add New Contact")

    name = st.text_input("Name")
    mobile = st.text_input("Mobile Number")
    email = st.text_input("Email Address")
    address = st.text_area("Address")
    category = st.selectbox(
        "Category", ["Personal", "Professional"]
    )

    if st.button("Add Contact"):
        if name and mobile and email and address:
            contact = {
                "Name": name,
                "Mobile": mobile,
                "Email": email,
                "Address": address,
                "Category": category
            }

            st.session_state.contacts.append(contact)
            st.success("Contact added successfully!")
        else:
            st.warning("Please fill all the fields.")

# View Contacts
elif menu == "View Contacts":

    st.header("All Contacts")

    if st.session_state.contacts:
        df = pd.DataFrame(st.session_state.contacts)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No contacts available.")

# Search Contact
elif menu == "Search Contact":

    st.header("Search Contact")

    search = st.text_input("Enter contact name")

    if st.button("Search"):
        found = False

        for contact in st.session_state.contacts:
            if search.lower() in contact["Name"].lower():
                st.write(contact)
                found = True

        if not found:
            st.error("Contact not found.")

# Update Contact
elif menu == "Update Contact":

    st.header("Update Contact")

    names = [c["Name"] for c in st.session_state.contacts]

    if names:
        selected = st.selectbox("Select Contact", names)

        if st.button("Load Contact"):
            st.session_state.edit_contact = selected

        if st.session_state.get("edit_contact") == selected:
            contact = next(
                c for c in st.session_state.contacts
                if c["Name"] == selected
            )

            new_name = st.text_input("Name", contact["Name"])
            new_mobile = st.text_input("Mobile", contact["Mobile"])
            new_email = st.text_input("Email", contact["Email"])
            new_address = st.text_area("Address", contact["Address"])
            new_category = st.selectbox(
                "Category",
                ["Personal", "Professional"],
                index=["Personal", "Professional"].index(
                    contact["Category"]
                )
            )

            if st.button("Update Contact"):
                contact["Name"] = new_name
                contact["Mobile"] = new_mobile
                contact["Email"] = new_email
                contact["Address"] = new_address
                contact["Category"] = new_category

                st.session_state.edit_contact = None
                st.success("Contact updated successfully!")
                st.rerun()
    else:
        st.info("No contacts available.")

# Delete Contact
elif menu == "Delete Contact":

    st.header("Delete Contact")

    names = [c["Name"] for c in st.session_state.contacts]

    if names:
        selected = st.selectbox("Select Contact to Delete", names)

        if st.button("Delete Contact"):
            for contact in st.session_state.contacts:
                if contact["Name"] == selected:
                    st.session_state.contacts.remove(contact)
                    break

            st.success("Contact deleted successfully!")
            st.rerun()
    else:
        st.info("No contacts available.")