import React from "react"

import { NextPage } from "next"

interface IAuthLayout {
  login: React.ReactNode
  register: React.ReactNode
}

const AuthLayout: NextPage<IAuthLayout> = ({ login, register }) => {
  const isLoggedIn = true

  return <div>{isLoggedIn ? login : register}</div>
}

export default AuthLayout
