import streamlit as st
from metro_graph import create_metro_graph, get_cities
from shortest_path import dijkstra

st.set_page_config(page_title="Metro Journey Planner", layout="centered")

st.title("🚇 Metro Journey Planner")
st.subheader("Mumbai & Pune Metro")

city = st.selectbox("Select City", get_cities())

graph = create_metro_graph(city)

if graph:
    stations = list(graph.nodes)

    source = st.selectbox("Source Station", stations)
    destination = st.selectbox("Destination Station", stations)

    if st.button("Find Shortest Path"):
        if source == destination:
            st.warning("Source and destination cannot be same.")
        else:
            distance, path = dijkstra(graph, source, destination)

            if path:
                st.success(f"Shortest Distance: {distance} km")
                st.write("➡️ Route:")
                st.write(" → ".join(path))
            else:
                st.error("No path found.")
