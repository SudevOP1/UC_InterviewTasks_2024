from django.shortcuts import render
import requests
from django.conf import settings

# Home Page
def index(request):
    return render(request, "index.html")

# Task-1
# Django Unchained Details (Using API)
def django_unchained_details(request):
    query = "Django Unchained"
    api_key = settings.MOVIES_API_KEY
    response = requests.get(f"https://www.omdbapi.com/?t={query}&apikey={api_key}")
    movie_details = response.json()
    return render(request, "django_unchained_details.html", {"django_unchained_details": movie_details})

# Task-2
# Searching Movies
def search_results(request):
    query = request.GET.get('query')
    if query:
        api_key = settings.MOVIES_API_KEY
        
        # Checking for perfect name match
        exact_match_response = requests.get(f"https://www.omdbapi.com/?t={query}&apikey={api_key}")
        exact_match = exact_match_response.json()
        
        if exact_match.get('Response') == "True" and exact_match.get('Title') == query:
            # Perfect match found
            return render(request, "django_unchained_details.html", {"django_unchained_details": exact_match})
        else:
            # No perfect match found, show movies with related names
            related_movies_response = requests.get(f"https://www.omdbapi.com/?s={query}&apikey={api_key}")
            related_movies = related_movies_response.json()
            return render(request, "search_results.html", {"search_results": related_movies, "query": query})
    
    # If no query is provided, render the search_results template with empty results
    return render(request, "search_results.html", {"search_results": {}, "query": query})
