import networkx as nx

def create_metro_graph(city):
    G = nx.Graph()

    if city == "Mumbai":
        stations = [
            "Andheri West", "Andheri East", "Ghatkopar",
            "Versova", "DN Nagar", "Lower Parel",
            "Wadala", "Chembur", "Vikhroli"
        ]

        connections = [
            ("Versova", "DN Nagar", 3),
            ("DN Nagar", "Andheri West", 2),
            ("Andheri West", "Lower Parel", 10),
            ("Lower Parel", "Wadala", 6),
            ("Wadala", "Chembur", 4),
            ("Chembur", "Ghatkopar", 3),
            ("Ghatkopar", "Vikhroli", 4),
            ("Andheri East", "Ghatkopar", 5)
        ]

    elif city == "Pune":
        stations = [
            "PCMC", "Sant Tukaram Nagar", "Bhosari",
            "Shivaji Nagar", "Civil Court",
            "Swargate", "Hadapsar", "Katraj"
        ]

        connections = [
            ("PCMC", "Sant Tukaram Nagar", 4),
            ("Sant Tukaram Nagar", "Bhosari", 3),
            ("Bhosari", "Shivaji Nagar", 6),
            ("Shivaji Nagar", "Civil Court", 2),
            ("Civil Court", "Swargate", 5),
            ("Swargate", "Katraj", 6),
            ("Civil Court", "Hadapsar", 7)
        ]

    else:
        return None

    for station in stations:
        G.add_node(station)

    for u, v, w in connections:
        G.add_edge(u, v, weight=w)

    return G


def get_cities():
    return ["Mumbai", "Pune"]
