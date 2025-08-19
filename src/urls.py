"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from ninja.responses import Response
from ninja import NinjaAPI

api = NinjaAPI(
  title="Health Check API",
  version="1.0.0",
  description="最小化的 Django Ninja API 模板"
)

@api.get("/health")
def health_check(request):
  """
  健康檢查端點
  返回服務狀態信息
  """
  health_data = {
      "status": "healthy",
      "message": "Service is running",
      "timestamp": "2024-08-19T11:09:00Z"
  }
  
  return Response(
      data=health_data,
      status=200,
      headers={"content_type": "application/json"}
  )

urlpatterns = [
    path("", api.urls),
]
