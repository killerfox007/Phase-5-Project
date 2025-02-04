import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { GoogleOAuthProvider } from '@react-oauth/google';
import store from './store';
import { Provider } from 'react-redux'

createRoot(document.getElementById('root')).render(
  <GoogleOAuthProvider clientId="538604332355-9dua4smq0rrh8bi6kcjudnq7b1oau0b4.apps.googleusercontent.com">
  <Provider store={store}>
  <StrictMode>
    <App />
  </StrictMode>,
  </Provider>
  </GoogleOAuthProvider>
)
