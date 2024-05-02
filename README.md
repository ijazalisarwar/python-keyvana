Rest API to Azure Data Lake Movement

We will create these two resources on Azure Portal.

1.	Azure Resource Group
2.	Azure Data Factory V2
 

3.	Azure Data Lake Storage Gen2
 



We will perform these tasks to edit Azure Data Factory:

•	Create Azure “Copy Data” task 
 


•	We will create Source and Destination connection to move data
•	Our Source Connection will be a RESTful API(GET) let me know if we will use any other restfully method. Input these type of data
-	Base URL
-	RESTful API Method (GET, POST)
-	Authentication type (Anonymous, Basic, Azure Key Vault, Service Principal)
   



•	Next, we will create Destination connection which will be “Azure Data Lake Gen2”

-	Service principal
-	Account key
-	Managed identity
	Once we test it we will give exact container path, where we will place the files.
 



Here we will give the container path
 



Then we will create properties of blob in Container
1-	Which file we will create it will be JSON in our case
2-	Is it a single object or an array of objects?
3-	Compression type and Encoding 
 


We will create a Schema Mapping
     


Once we run the pipeline we will get the JSON files in our destination container.
