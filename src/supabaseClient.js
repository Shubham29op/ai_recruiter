import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://glhqworqetvlhodgivmb.supabase.co'
const supabaseAnonKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdsaHF3b3JxZXR2bGhvZGdpdm1iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAyNzQzMDYsImV4cCI6MjA2NTg1MDMwNn0.FAYKfvKETg0LvFL2mOS7JJJbMg7MjFV1606tcZwwe_c'

export const supabase = createClient(supabaseUrl, supabaseAnonKey)
