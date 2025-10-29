
from typing import  List
from pydantic import BaseModel, Field, field_validator



class ChartPoint(BaseModel):
    month: str = Field(..., min_length=1)
    desktop: float

class AreaChart(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    trendLabel: str = Field(..., min_length=1)
    dateRangeLabel: str = Field(..., min_length=1)
    trendDirection: bool
    data: List[ChartPoint]

class AreaResponse(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    trendLabel: str = Field(..., min_length=1)
    dateRangeLabel: str = Field(..., min_length=1)
    trendDirection: bool 
    data: List[ChartPoint]

class BarChart(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    trendLabel: str = Field(..., min_length=1)
    dateRangeLabel: str = Field(..., min_length=1)
    trendDirection: bool
    data: List[ChartPoint]

class BarResponse(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    trendLabel: str = Field(..., min_length=1)
    dateRangeLabel: str = Field(..., min_length=1)
    trendDirection: bool
    data: List[ChartPoint]
    
class PieSlice(BaseModel):
    browser: str = Field(..., min_length=1)
    visitors: float
    fill: str = Field(..., min_length=1)

class PieChart(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    trendLabel: str = Field(..., min_length=1)
    dateRangeLabel: str = Field(..., min_length=1)
    trendDirection: bool 
    data: List[PieSlice]

class PieResponse(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    trendLabel: str = Field(..., min_length=1)
    dateRangeLabel: str = Field(..., min_length=1)
    trendDirection: bool  
    data: List[PieSlice]

class MultilinePoint(BaseModel):
    month: str = Field(..., min_length=1)
    desktop: float
    mobile: float

class MultiLineChart(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    trendLabel: str = Field(..., min_length=1)
    dateRangeLabel: str = Field(..., min_length=1)
    trendDirection: bool  
    data: List[MultilinePoint]  

class MultiLineResponse(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    trendLabel: str = Field(..., min_length=1)
    dateRangeLabel: str = Field(..., min_length=1)
    trendDirection: bool  
    data: List[MultilinePoint]



