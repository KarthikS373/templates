import { FC, ReactElement } from "react"
// Get authentication data from any source, in this case from context api, and check if user is admin
// import { Navigate } from 'react-router-dom';

interface IAdminGuardProps {
  children: ReactElement
}

const AdminGuard: FC<IAdminGuardProps> = ({ children }) => {
  // const { isAdmin } = <... logic to check isAdmin ...>

  // if (!isAdmin) {
  //   return <Navigate to="home" />;
  // }

  return children
}

export default AdminGuard
