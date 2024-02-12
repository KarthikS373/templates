import { Metadata } from "next"

import { Provider } from "@/providers"

import "@/styles/globals.css"

export const metadata: Metadata = {
  title: {
    default: "Title",
    template: "Title | %s",
  },
  description: "",
  verification: {
    me: "",
    google: "",
    yahoo: "",
  },
}

const RootLayout = ({
  children,
}: Readonly<{
  children: React.ReactNode
}>) => {
  return (
    <html lang="en">
      <body className="min-h-screen">
        <Provider>{children}</Provider>
      </body>
    </html>
  )
}

export default RootLayout
