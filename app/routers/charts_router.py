from operator import mul
from fastapi import Path, Query, APIRouter
from fastapi.responses import JSONResponse
from typing import Optional, List

from app.models.charts_model import AreaChart, AreaResponse, BarChart, BarResponse, MultiLineChart, MultiLineResponse, PieChart, PieResponse

charts_router = APIRouter()


area_chart = {
    "title": "",
    "description": "",
    "trendLabel": "",
    "dateRangeLabel": "",
    "trendDirection": True,
    "data": [],
}
bar_chart = {
    "title": "",    
    "description": "",
    "trendLabel": "",
    "dateRangeLabel": "",
    "trendDirection": True,
    "data": [],
}
pie_chart = {
    "title": "",
    "description": "",
    "trendLabel": "",
    "dateRangeLabel": "",
    "trendDirection": True,
    "data": [],
}

multiline_chart = {
    "title": "",
    "description": "",
    "trendLabel": "",
    "dateRangeLabel": "",
    "trendDirection": True,
    "data": [],
}

@charts_router.get("/area", tags=["ChartsGet"])
async def get_area_chart()->AreaResponse:
    return JSONResponse(content=area_chart, status_code=200)

@charts_router.put("/area", tags=["ChartsPut"])
async def put_area_chart(data: AreaChart):
    area_chart.update(**data.model_dump())
    
@charts_router.get("/bar", tags=["ChartsGet"])
async def get_bar_chart()->BarResponse:
    return JSONResponse(content=bar_chart, status_code=200)

@charts_router.put("/bar", tags=["ChartsPut"]) 
async def put_bar_chart(data: BarChart):
    bar_chart.update(**data.model_dump())

@charts_router.get("/pie", tags=["ChartsGet"])
async def get_pie_chart()->PieResponse:
    return JSONResponse(content=pie_chart, status_code=200)

@charts_router.put("/pie", tags=["ChartsPut"])
async def put_pie_chart(data: PieChart):
    pie_chart.update(**data.model_dump())

@charts_router.get("/multiline", tags=["ChartsGet"])
async def get_multiline_chart()->MultiLineResponse:
    return JSONResponse(content=multiline_chart, status_code=200)

@charts_router.put("/multiline", tags=["ChartsPut"])
async def put_multiline_chart(data: MultiLineChart):
    multiline_chart.update(**data.model_dump())





