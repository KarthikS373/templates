import React, { useMemo } from "react"

interface IUserContext {
  handleLogin: (email: string, password: string) => Promise<{ success: boolean; message: string }>
}

interface IUserProvider {
  children: React.ReactNode
}

const Context = React.createContext<IUserContext>({} as IUserContext)

/* Login User */
const handleLogin = async (
  email: string,
  password: string
): Promise<{ success: boolean; message: string }> => {
  if (email && password) return { success: true, message: "Login success" }

  return { success: false, message: "Login failed" }
}

const UserProvider = ({ children }: IUserProvider) => {
  const context = useMemo(
    () => ({
      handleLogin,
    }),
    []
  )

  return <Context.Provider value={context}>{children}</Context.Provider>
}

const useUserContext = () => {
  const c = React.useContext(Context)

  if (c === undefined) {
    throw new Error("useUserContext must be used within a UserProvider")
  }

  return c
}

export { UserProvider, useUserContext }
