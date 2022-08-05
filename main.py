from fastapi import Depends, FastAPI, HTTPException, status
from database import SessionLocal, create_db
from models import Graph as GraphModel
import uvicorn
from typing import Optional
from utils import (
    find_all_routes,
    min_route,
    format_graph_data,
    remove_duplicated_in_data,
    remove_same_source_and_target,
)
from schemas import Graph, GraphIn, Routes, MinRoute


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    create_db()
    print("Started")


@app.get("/graph/{graph_id}", response_model=Graph, status_code=status.HTTP_200_OK)
def get_a_graph(graph_id: int, db=Depends(get_db)):
    graph = db.query(GraphModel).filter(GraphModel.id == graph_id).first()
    if graph is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Graph not found"
        )
    return Graph(id=graph.id, data=graph.data)


@app.post("/create_graph", response_model=Graph, status_code=status.HTTP_201_CREATED)
def create_graph(graph: GraphIn, db=Depends(get_db)):
    formated_data = remove_same_source_and_target(remove_duplicated_in_data(graph.data))
    new_graph = GraphModel(data=formated_data)

    db.add(new_graph)
    db.commit()

    return new_graph


@app.post(
    "/routes/{graph_id}/from/{town_from}/to/{town_to}",
    response_model=Routes,
    status_code=status.HTTP_200_OK,
)
def all_routes_between_nodes(
    graph_id: int,
    town_from: str,
    town_to: str,
    maxStops: Optional[int] = 10**99,
    db=Depends(get_db),
):
    graph = db.query(GraphModel).filter(GraphModel.id == graph_id).first()
    if graph is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Graph not found"
        )
    row_routes = find_all_routes(
        format_graph_data(graph.data), town_from, town_to, maxStops
    )
    formated_routes_data = []
    for row_route in row_routes:
        formated_routes_data.append(
            {"route": "".join(row_route), "stops": len(row_route) - 1}
        )
    response = Routes(routes=formated_routes_data)
    return response


@app.post(
    "/distance/{graph_id}/from/{town_from}/to/{town_to}",
    response_model=MinRoute,
    status_code=status.HTTP_200_OK,
)
def min_route_between_nodes(
    graph_id: int,
    town_from: str,
    town_to: str,
    db=Depends(get_db),
):
    if town_from == town_to:
        return MinRoute(distance=0, path=[town_from])
    graph = db.query(GraphModel).filter(GraphModel.id == graph_id).first()
    if graph is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Graph not found"
        )
    route = min_route(format_graph_data(graph.data), town_from, town_to, max_steps=3)

    if route["path"] == []:
        return MinRoute(distance=-1, path=[])

    response = MinRoute(distance=route["distance"], path=route["path"])
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8080, host="0.0.0.0")
