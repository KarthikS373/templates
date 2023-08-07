import { createBrowserRouter, RouterProvider } from "react-router-dom"

import React from "react"

import ReactQuery from "@plugins/react-query"
import { UserProvider } from "@providers/user"
import routes from "@routes/index"

const router = createBrowserRouter(routes)

const App = () => {
  return (
    <ReactQuery>
      <UserProvider>
        <RouterProvider router={router} />
      </UserProvider>
    </ReactQuery>
  )
}

export default App
