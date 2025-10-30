from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Dict, Any

from app.models.charts_model import (
    AreaChart, AreaResponse,
    BarChart, BarResponse,
    PieChart, PieResponse,
    MultiLineChart, MultiLineResponse
)

charts_router = APIRouter()

charts_store: Dict[str, Dict[str, Any]] = {
    "area": {"title": "", "description": "", "trendLabel": "", "dateRangeLabel": "", "trendDirection": True, "data": []},
    "bar": {"title": "", "description": "", "trendLabel": "", "dateRangeLabel": "", "trendDirection": True, "data": []},
    "pie": {"title": "", "description": "", "trendLabel": "", "dateRangeLabel": "", "trendDirection": True, "data": []},
    "multiline": {"title": "", "description": "", "trendLabel": "", "dateRangeLabel": "", "trendDirection": True, "data": []},
}

def get_chart(chart_name: str):
    return JSONResponse(content=charts_store[chart_name], status_code=200)

def put_chart(chart_name: str, data):
    charts_store[chart_name].update(**data.model_dump())
    return JSONResponse(content={"message": f"{chart_name} chart updated"}, status_code=200)


@charts_router.get("/area", tags=["ChartsGet"])
async def get_area_chart() -> AreaResponse:
    return get_chart("area")

@charts_router.put("/area", tags=["ChartsPut"])
async def put_area_chart(data: AreaChart):
    return put_chart("area", data)


@charts_router.get("/bar", tags=["ChartsGet"])
async def get_bar_chart() -> BarResponse:
    return get_chart("bar")

@charts_router.put("/bar", tags=["ChartsPut"])
async def put_bar_chart(data: BarChart):
    return put_chart("bar", data)


@charts_router.get("/pie", tags=["ChartsGet"])
async def get_pie_chart() -> PieResponse:
    return get_chart("pie")

@charts_router.put("/pie", tags=["ChartsPut"])
async def put_pie_chart(data: PieChart):
    return put_chart("pie", data)


@charts_router.get("/multiline", tags=["ChartsGet"])
async def get_multiline_chart() -> MultiLineResponse:
    return get_chart("multiline")

@charts_router.put("/multiline", tags=["ChartsPut"])
async def put_multiline_chart(data: MultiLineChart):
    return put_chart("multiline", data)

@charts_router.get("/delete-all-charts", tags=["ChartsDelete"])
async def delete_all_charts():
    for chart in charts_store.values():
        chart.update(title="", description="", trendLabel="", dateRangeLabel="", trendDirection=True, data=[])
    return JSONResponse(content={"message": "All charts deleted"}, status_code=200)
