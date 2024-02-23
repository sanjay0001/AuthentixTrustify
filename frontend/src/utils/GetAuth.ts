function getCookie(cookieName: string): string | null {
    // Split the document.cookie string into individual cookie pairs
    const cookies: string[] = document.cookie.split('; ');

    // Iterate through the cookie pairs to find the desired cookie
    for (const cookie of cookies) {
        const [name, value] = cookie.split('=');

        // Check if the cookie name matches the provided cookieName
        if (name === cookieName) {
            // Return the value of the cookie
            return decodeURIComponent(value);
        }
    }

    // If the cookie is not found, return null
    return null;
}

export function getCSRFToken(): string | null{
    return getCookie("csrftoken")
}

export function getSessionId(): string | null{
    return getCookie("sessionid")
}