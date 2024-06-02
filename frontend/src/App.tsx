import { Box, ThemeProvider } from '@mui/system';
import React from 'react';
import { theme } from './utilities/theme';
import { ViewDebug } from './views/ViewDebug/ViewDebug';
import { RouterProvider } from 'react-router-dom';
import { router } from './views/router';

export const App: React.FC = () => {
    return (
        <ThemeProvider theme={theme}>
            <Box sx={{
                height: "100vh",
                width: "100vw",
                backgroundColor: "background.main",
                color: "background.accentColor",
            }}>
            <RouterProvider router={router} />
            </Box>
        </ThemeProvider>
    );
}

