from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, text
from typing import Optional

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# SQLite database
engine = create_engine("sqlite:///movies.sqlite")



@app.get("/", response_class=HTMLResponse)
async def home(
    request: Request,
    search: Optional[str] = Query(None),             # Search only original_title
    min_rating: Optional[float] = Query(None),       # Filters
    max_rating: Optional[float] = Query(None),
    min_budget: Optional[int] = Query(None),
    max_budget: Optional[int] = Query(None),
    year: Optional[str] = Query(None)
):
    query = "SELECT * FROM movies WHERE 1=1"
    params = {}

    # === SEARCH ===
    if search and search.strip():
        query += " AND LOWER(original_title) LIKE LOWER(:search)"
        params["search"] = f"%{search.strip()}%"

    # === FILTERS ===
    if min_rating is not None:
        query += " AND vote_average >= :min_rating"
        params["min_rating"] = min_rating
    if max_rating is not None:
        query += " AND vote_average <= :max_rating"
        params["max_rating"] = max_rating

    if min_budget is not None:
        query += " AND budget >= :min_budget"
        params["min_budget"] = min_budget
    if max_budget is not None:
        query += " AND budget <= :max_budget"
        params["max_budget"] = max_budget

    if year and year.strip():
        query += " AND release_date LIKE :year"
        params["year"] = f"{year.strip()}%"

    with engine.connect() as conn:
        results = conn.execute(text(query), params).fetchall()

    return templates.TemplateResponse("index.html", {"request": request, "movies": results})