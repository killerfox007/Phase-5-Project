import React from 'react'
import { AppBar, Toolbar, Button, Typography, Container } from '@mui/material'
import { Link } from "react-router-dom"

function nav() {
  return (
    <AppBar position="static" sx={{ backgroundColor: '#013220' }}>
        <Container maxWidth="lg">
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>
            Girl Scout's Cookies Placeholder
          </Typography>
          <Button component={Link} to='/' sx={{ color: '#FFFFFF' }}>
            Home
          </Button>
          <Button component={Link} to='/signup' sx={{ color: '#FFFFFF' }}>
            Login
          </Button>
          
        </Toolbar>
      </Container>
    </AppBar>
  )
}


export default nav