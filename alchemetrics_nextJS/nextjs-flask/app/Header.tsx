// components/Header.tsx
import React from 'react';
import Link from 'next/link';
import HeaderCSS from './Header.module.css';

const Header: React.FC = () => {
    return (
        <div className={HeaderCSS.Header}>
            <nav>
                <Link href="/">Home</Link> | <Link href="/Inventory">Inventory</Link> | <Link href="/archive">Archive</Link>
            </nav>
        </div>
    );
}

export default Header;