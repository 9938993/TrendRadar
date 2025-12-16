#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TrendRadar API Entry Point for Vercel Serverless Function

This file serves as the entry point for the TrendRadar serverless function
on Vercel platform. It redirects requests to the main application.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from main import app, startup
    
    # Run startup on module import
    startup()
    
    # Export the ASGI app for Vercel
    handler = app
    
except Exception as e:
    # Fallback response if main.py fails to load
    async def handler(request):
        return {
            'statusCode': 500,
            'body': f'Error loading application: {str(e)}'
        }
