library(sp)
library(rgdal)
library(leaflet)
library(broom)
library(RColorBrewer)
library(htmlwidgets)
library(leaflet.extras)
root <- "C:/HTML Files/FosbergSite"
setwd(root)


jsonFile <- "FosbergFire-bba334df2ba6.json"
jsonPath <- paste(root, jsonFile, sep = "/")

Sys.setenv(GCS_AUTH_FILE = jsonPath)
library(googleCloudStorageR)

googleAuthR::gar_auth_service("FosbergFire-bba334df2ba6.json") 

proj <- "fosbergfire-209406"
Fosbergbucket <- "www.fosbergfire.com"

dataName = "data.csv"
dataFile <- gcs_get_object("data.csv", bucket = Fosbergbucket, saveToDisk = dataName, overwrite = TRUE)




#reading shapefile and data file
cali <- readOGR("C:/Users/brian/R_Programs/Shapefile","CA_Counties_TIGER2016")
caliData <- read.csv(dataName, header = TRUE, sep = ",")
caliMerged <- merge(cali, caliData, by.x = "NAME", by.y = "County")



#recreates dataframe with correct coordinate system
cali_WGS84 <- spTransform(caliMerged, CRS("+proj=longlat +init=epsg:4326"))



#functions to set the coloring for map scale
palFun <- colorNumeric(palette = "YlOrRd", domain = cali_WGS84$Index)
palFunB <- colorQuantile(palette = "YlOrRd", domain = cali_WGS84$Index, n = 5)



#functions for popup text including HTML elements for links to external websites
popupText <- paste("<strong>County: </strong>", cali_WGS84$NAME, "<br>", "<strong>Fosberg Index: </strong>", cali_WGS84$Index, "<br>",
                   "<a href ='", cali_WGS84$Websites, "' target = '_blank'>County Website</a>")


#map code and styling
calimap <- leaflet(cali_WGS84) %>% 
addPolygons(stroke = TRUE, color = "black", weight = 0.7, fillColor = ~palFun(Index), fillOpacity = 0.8,
smoothFactor = 0.5, popup = popupText, group = "California") %>%
addTiles(group = "Light Street Map") %>% 
addProviderTiles("CartoDB.DarkMatter", group = "Dark Street Map") %>%
addProviderTiles("Stamen.Terrain", group = "Terrain") %>%
addLegend(position = "bottomleft", pal = palFun, values = ~Index, title = "Fosberg Fire Index") %>%
addLayersControl(baseGroups = c("Light Street Map", "Dark Street Map", "Terrain"), overlayGroups = c("California")) %>%
suspendScroll()



#saves file to a specific HTML file as specified by f

#outputFile <- "test.html"

f <- "C:\\Users\\brian\\PycharmProjects\\FosbergFire\\test.html"
saveWidget(calimap, file.path(normalizePath(dirname(f)),basename(f)))
#saveWidget(calimap, outputFile)

#gcs_upload(outputFile, bucket = Fosbergbucket, name = outputGCSFile)
