from app.views import *

from django.urls import path
urlpatterns = [
    path("",home, name="home"),
    path("about/",about, name="about"),
    path("service/",service, name="service"),
    path("contact/",contact, name="contact"),
    path("donate/",donate, name="donate"),
    path("partner/",partner, name="partner"),
    path("pastjob/",pastjob, name="pastjob"),
    path("jobdetail/<pk>/",jobdetail, name="jobdetail"),
    path("press/",press, name="press"),
    path("newdetail/<pk>/",newdetail, name="newdetail"),
    path("ourteam/",ourteam, name="ourteam"),
    path("newstory/",newstory, name="newstory"),
    path("project/",project, name="project"),
    path("pubdetail/<pk>/",pubdetail, name="pubdetail"),
    path("prodetail/<pk>/",prodetail, name="prodetail"),
    path("Pressdetail/<pk>/",Pressdetail, name="Pressdetail"),
    path("publications/",publications, name="publications"),
    path("report/",report, name="report"),
    path("traning/",traning, name="traning"),
    path("projectupdate/",projectupdate, name="projectupdate"),
    path("siteclinic/",siteclinic, name="siteclinic"),
    
    
    
    # User_dashboard
    path("dashboard/<pk>/",dashboard, name="dashboard"),
    path("usercreate/<pk>/",usercreate, name="usercreate"),
    path("userdelete/<pk>/",userdelete, name="userdelete"),
    path("userupdate/<pk>/",userupdate, name="userupdate"),
    
    # job
    path("jobclient/<pk>/",jobclient, name="jobclient"),
    path("jobdeletex/<pk>/",jobdeletex, name="jobdeletex"),
    path("jobcreate/<pk>/",jobcreate, name="jobcreate"),
    path("jobupdate/<pk>/",jobupdate, name="jobupdate"),
    
    
    
    # reportDetail
    
    path("reportDetail/<pk>/",reportDetail, name="reportDetail"),
    path("updatereport/<pk>/",updatereport, name="updatereport"),
    path("reportdeletex/<pk>/",reportdeletex, name="reportdeletex"),
    path("reportcreate/<pk>/",reportcreate, name="reportcreate"),
    
    # detailteam
    
    path("detailteam/<pk>/",detailteam, name="detailteam"),
    path("teamdeletex/<pk>/",teamdeletex, name="teamdeletex"),
    path("updateteam/<pk>/",updateteam, name="updateteam"),
    path("createteam/<pk>/",createteam, name="createteam"),
    
    # bank?
    
    path("bankdeletex/<pk>/",bankdeletex, name="bankdeletex"),
    path("createbank/<pk>/",createbank, name="createbank"),
    path("bankDetail/<pk>/",bankDetail, name="bankDetail"),
    path("updatebank/<pk>/",updatebank, name="updatebank"),
    
    # projectdetal
    
    path("projectdetal/<pk>/",projectdetal, name="projectdetal"),
    path("projectdeletex/<pk>/",projectdeletex, name="projectdeletex"),
    path("createproject/<pk>/",createproject, name="createproject"),
    path("yupdateproject/<pk>/",yupdateproject, name="yupdateproject"),
    
    # pressdeletex
    path("pressdeletex/<pk>/",pressdeletex, name="pressdeletex"),
    path("pressDetail/<pk>/",pressDetail, name="pressDetail"),
    path("createpress/<pk>/",createpress, name="createpress"),
    path("updatepress/<pk>/",updatepress, name="updatepress"),
    
    
    
    # publicationsx
    path("createpublications/<pk>/",createpublications, name="createpublications"),
    path("publicationsxDetail/<pk>/",publicationsxDetail, name="publicationsxDetail"),
    path("updatepublications/<pk>/",updatepublications, name="updatepublications"),
    path("publicationsxdeletex/<pk>/",publicationsxdeletex, name="publicationsxdeletex"),
    
    # newsdeletex
    
    path("newsdeletex/<pk>/",newsdeletex, name="newsdeletex"),
    path("newdetail/<pk>/",newdetail, name="newdetail"),
    path("createnews/<pk>/",createnews, name="createnews"),
    path("updatenews/<pk>/",updatenews, name="updatenews"),
    
    
    
     
    # aboutsite?
    
    path("aboutsite/<pk>/",aboutsite, name="aboutsite"),
    
    # site
    path("site/<pk>/",site, name="site"),
    
    
    path("accounts/login/",Loginuser, name="Loginuser"),
    path("register/",registeruser, name="registeruser"),
    path("logoutuser/",logoutuser, name="logoutuser"),

]