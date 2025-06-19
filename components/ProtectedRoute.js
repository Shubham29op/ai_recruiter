import { useEffect, useState } from 'react';
import { Navigate } from 'react-router-dom';
import { supabase } from '../supabaseClient';

export default function ProtectedRoute({ roleRequired, children }) {
  const [loading, setLoading] = useState(true);
  const [hasAccess, setHasAccess] = useState(false);

  useEffect(() => {
    const checkAccess = async () => {
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) {
        setHasAccess(false);
        setLoading(false);
        return;
      }

      const { data, error } = await supabase
        .from('users')
        .select('role')
        .eq('id', user.id)
        .single();

      if (data?.role === roleRequired) {
        setHasAccess(true);
      } else {
        setHasAccess(false);
      }

      setLoading(false);
    };

    checkAccess();
  }, [roleRequired]);

  if (loading) return <div>Loading...</div>;

  return hasAccess ? children : <Navigate to="/" />;
}
