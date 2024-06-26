import React, {useEffect} from 'react';
import { Link as RouterLink } from 'react-router-dom';
import { Link } from '@mui/material';
import { AppBar, Toolbar, IconButton, Box} from '@mui/material';
import { ThemeProvider } from '@mui/material/styles';
import MenuRoundedIcon from '@mui/icons-material/MenuRounded';
import { NVTheme } from './Theme/NavigationBarTheme';
import Devnavlinkcomplex from "./devnavlinkcomplex";
import Usernavlinkcomplex from "./usernavlinkomplex";
import {useRecoilState} from "recoil";
import {loginState} from '../../atom/atom';
import api from "../../axios";
import {useRecoilValue} from "recoil";
import {usernameState} from "../../atom/atom";

function NavigationBar({ isMobile, handleDrawerToggle }) {
    const login = useRecoilValue(loginState);
    const isdev = true;
    const [username, setUsername] = useRecoilState(usernameState);

    const fetchUsername = async () => {
        if(login){
            try {
                const response = await api.get('/accounts/dj-rest-auth/user/');
                setUsername(response.data.pk);
            } catch (error) {
                console.error('Failed to fetch username:', error);
            }
        }

    }

    useEffect(() => {
        fetchUsername();
    }, []);

    useEffect(() => {
        console.log(username);
    }, [username]);

    return (
        <ThemeProvider theme={NVTheme}>
        <AppBar position="static" elevation={0}>
            <Toolbar style={{ display: 'flex' }}>
                <Link component={RouterLink} to="/" sx={{
                    display: 'inline-flex',
                    alignItems: 'center',
                    color: 'inherit',
                    textDecoration: 'none',
                    padding: '0px',
                    marginRight: '5%',
                    marginLeft: '5%',
                    transition: 'color 0.3s ease',
                    '&:hover': {
                        color: '#999999',
                        cursor: 'pointer'
                    },
                    '@media (max-width: 768px)': {
                        margin: '0',
                    }
                }}>
                    <img alt="" src="/transparentCc.png" width="30" height="30" style={{ verticalAlign: 'middle' }} />
                    𝑪𝒖𝒓𝒕𝒂𝒊𝒏𝑪𝒂𝒍𝒍
                </Link>
                {isMobile ? (
                    <IconButton color="inherit" aria-label="open drawer" edge="end" onClick={handleDrawerToggle} sx={{ marginLeft: 'auto' }}>
                        <MenuRoundedIcon fontSize={"large"}/>
                    </IconButton>
                ) : (
                    <Box sx={{ display: 'flex', justifyContent: 'center' }}>
                        {isdev ? <Devnavlinkcomplex username={username}/> : <Usernavlinkcomplex username={username}/>}
                    </Box>
                )}
            </Toolbar>
        </AppBar>
        </ThemeProvider>
    );
}

export default NavigationBar;