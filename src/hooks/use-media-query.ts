import { useEffect, useState } from "react"

const useMediaQuery = (query: string): boolean => {
  const getMatches = (q: string): boolean => {
    // Prevents SSR issues
    if (typeof window !== "undefined") {
      return window.matchMedia(q).matches
    }
    return false
  }

  const [matches, setMatches] = useState<boolean>(getMatches(query))

  useEffect(() => {
    const handleChange = () => {
      setMatches(getMatches(query))
    }

    const matchMedia = window.matchMedia(query)

    handleChange()

    matchMedia.addEventListener("change", handleChange)

    return () => {
      matchMedia.removeEventListener("change", handleChange)
    }
  }, [query])

  return matches
}

export default useMediaQuery
