GRAPH_API_URL=http://localhost:4001/api-json

openapi-generator generate \
  -g python-nextgen \
  -i $GRAPH_API_URL \
  -o project_chiral_ai_service/api \
  --additional-properties=packageName=graph_api,generateSourceCodeOnly=true
