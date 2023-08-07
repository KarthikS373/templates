import { FC, ReactElement } from "react"

// Get authentication data from any source, in this case from context api, and check if user is authenticated
// and redirect to main page if not or show loading page if it is still loading.

// import { Navigate } from 'react-router-dom';

interface IGuestGuardProps {
  children: ReactElement
}

const GuestGuard: FC<IGuestGuardProps> = ({ children }) => {
  // const { isAuthenticated, isLoading } = <... logic to check isAuth and isLoading ...>

  // if (isLoading) {
  //   return <LoadingPage />;
  // }

  // if (isAuthenticated) {
  //   return <Navigate to="/app/home" />;
  // }

  return children
}

export default GuestGuard
