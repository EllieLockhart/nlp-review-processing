from py2neo import GraphService
import os

bolt_url = os.getenv("GRAPHSERVICE")
bolt_user = os.getenv("GRAPHUSER")
bolt_pass = os.getenv("GRAPHPASS")

graph = GraphService(auth=(bolt_user, bolt_pass), host=bolt_url)

tx = graph.begin()
tx.append("CREATE (media:MediaArtifact full_title: $game) RETURN media", game=game)