import streamlit as st

def main():
    st.markdown(
        """
        <style>
        .custom-sidebar {
            position: fixed;
            left: 0;
            top: 0;
            height: 100%;
            width: 200px;
            background-color: #f0f0f0;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="custom-sidebar">
            <h3>Custom Sidebar</h3>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.title("Main Content")
    st.write("This is the main content area.")

if __name__ == "__main__":
    main()
